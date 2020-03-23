# The `file` Command

This document provides some additional information on the `file` command.  Much
of this information was pulled directly from the manual page (`man file`).

We show a deep dive into the `file` command to demonstrate the importance of
understanding the fundamentals that your forensic tools are built upon.  Often
tools are dependent on their configuration, or rule set.  By understanding the
underlying technique you can then improve your tool's effectiveness or address
corner cases where it fails.

## Background

The `file` command attempts to classify the type of a file by performing
a series of tests.

> There are three sets of tests, performed in this order
1. filesystem tests
2. magic tests
3. language tests

## filesystem tests
> based on examining the return from a stat(2) system call. 

> known file types (sockets, symbolic links, or named pipes ) are intuited if
> they are defined in the system header file `<sys/stat.h>`

Snippet from  `/usr/include/linux/stat.h`
```
i#define S_IFBLK  0060000
#define S_IFDIR  0040000
#define S_IFCHR  0020000
#define S_IFIFO  0010000
#define S_ISUID  0004000
#define S_ISGID  0002000
#define S_ISVTX  0001000

#define S_ISLNK(m)      (((m) & S_IFMT) == S_IFLNK)
#define S_ISREG(m)      (((m) & S_IFMT) == S_IFREG)
#define S_ISDIR(m)      (((m) & S_IFMT) == S_IFDIR)
#define S_ISCHR(m)      (((m) & S_IFMT) == S_IFCHR)
#define S_ISBLK(m)      (((m) & S_IFMT) == S_IFBLK)
#define S_ISFIFO(m)     (((m) & S_IFMT) == S_IFIFO)
#define S_ISSOCK(m)     (((m) & S_IFMT) == S_IFSOCK)

#define S_IRWXU 00700
#define S_IRUSR 00400
```

### Example: symlink
Create a file. Make a symbolic link (a special type of os file). Verify
information with `stat` command. Show output of `file` command.

```
$ echo "hello" > a

$ cat a
hello

$ ln -s a b

$ ls -l
total 4
-rw-rw-r-- 1 dfir dfir 6 Jan 24 15:48 a
lrwxrwxrwx 1 dfir dfir 1 Jan 24 15:49 b -> a

$ cat b
hello

$ stat b
  File: 'b' -> 'a'
  Size: 1               Blocks: 0          IO Block: 4096   symbolic link
Device: 801h/2049d      Inode: 1842194     Links: 1
Access: (0777/lrwxrwxrwx)  Uid: ( 1000/    dfir)   Gid: ( 1000/    dfir)
Access: 2018-01-24 15:49:11.002758957 +0000
Modify: 2018-01-24 15:49:09.130770952 +0000
Change: 2018-01-24 15:49:09.130770952 +0000
 Birth: -

$ file b
b: symbolic link to a
```

## magic tests

> used to check for files with data in particular fixed formats

> a "magic number" stored in a particular place near the beginning of the file
> that tells the UNIX operating system...

> Any file with some invariant identifier at a small fixed offset into the file
> can usually be described in this way.

Sources (or use `-m` to specify):
- `/etc/magic`
- `/usr/share/misc/magic.mgc` (compiled magic file)
- `$HOME/.magic.mgc` (compiles magic file)
- `$HOME/.magic`

Information on the magic format can be viewed in it's manual page (`man magic`).

> Each line of a fragment file specifies a test to be performed.  A test
> compares the data starting at a particular offset in the file with a byte
> value, a string or a numeric value.  If the test succeeds, a message is
> printed.

> Some file formats contain additional information which is to be printed along
> with the file type or need additional tests to determine the true file type.
> These additional tests are introduced by one or more `>` characters preceding
> the offset.  The number of `>` on the line indicates the level of the test;
> a line with no > at the beginning is considered to be at level 0.  Tests are
> arranged in a tree-like hierarchy: if the test on a line at level n succeeds,
> all following tests at level n+1 are performed, and the messages printed if
> the tests succeed, until a line with level n (or less) appears. For more
> complex files, one can use empty messages to get just the "if/then" effect, in
> the following way:

```
           0      string   MZ
           >0x18  leshort  <0x40   MS-DOS executable
           >0x18  leshort  >0x3f   extended PC executable (e.g., MS Windows)
```

Examples of magic files are available in the [source mirror][mirror].

[mirror]:https://github.com/file/file/tree/master/magic/Magdir


### Example: `filesystems` magic

What follow are snippets from the magic file used to identify filesystems
([reference][ref]). A visual example of a Windows 7 MBR as referenced in the
comment can be viewed [here][viz]. A labeled breakdown of the MBR format is also
available from [Invoke-IR][ir]

[ref]:https://github.com/file/file/blob/c4c9192da7cc8dc7728f6520457a5d6200881905/magic/Magdir/filesystems
[viz]:http://thestarman.pcministry.com/asm/mbr/W7MBR.htm#CHS
[ir]:https://camo.githubusercontent.com/af9e51533b78223e3e588dfa195f7a0779a20552/68747470733a2f2f63646e2e7261776769742e636f6d2f496e766f6b652d49522f466f72656e736963506f73746572732f6d61737465722f7372632f426f6f74536563746f72732f4d6173746572426f6f745265636f72642e737667

```
#------------------------------------------------------------------------------
# $File: filesystems,v 1.124 2018/01/12 12:35:30 christos Exp $
# filesystems:  file(1) magic for different filesystems
```

At offset `0x1FE` test for `0xAA55` (little-endian). The end of MBR
marker.
```
0x1FE          leshort         0xAA55           DOS/MBR boot sector
```

Starting at offset 0 search the next 2 bytes for the string corresponding to the
boot code assembly.
```
# added by Joerg Jenderek at Feb 2013 according to http://thestarman.pcministry.com/asm/mbr/
# and http://en.wikipedia.org/wiki/Master_Boot_Record
# test for nearly all MS-DOS Master Boot Record initial program loader (IPL) is now done by
# characteristic assembler instructions: xor ax,ax;mov ss,ax;mov sp,7c00
>0  search/2  \x33\xc0\x8e\xd0\xbc\x00\x7c  MS-MBR
```

Identify Windows 7 boot code based on unique assembler sequence.
```
# Microsoft Windows 7 (http://thestarman.pcministry.com/asm/mbr/W7MBR.htm)
# assembler instructions: cmp ebx,"TCPA";cmp
>>>0xEC   ubequad 0x6681fb5443504175    Windows 7
# where xxyyzz are lower bits from offsets of error messages varying for
different languages
>>>>0x1B4 ubelong&0x00FFFFFF  0x00637b9a  english
```

Compute a relative offset by reading the value at index `0x1b5` and adding
`0x100` to that. This is the start of the error message. The read a string from
this offset until a null byte (`\0`).
```
# "Invalid partition table"       xx=0x163 for english version
>>>>0x1b5 ubyte   >0      at offset 0x1%x
>>>>(0x1b5.b+0x100) string  >\0     "%s"
```

The rest of the output continues in this format. By matching similar rules
resulting in an output string like `DOS/MBR boot sector MS-MBR Windows 7 english
at offset 0x163 "Invalid partition table"...`

## language tests

> If a file does not match any of the entries in the magic file, it is examined
> to see if it seems to be a text file.

> Once file has determined the character set used in a text-type file, it will
> attempt to determine in what language the file is written. 

> For example, the keyword .br indicates that the file is most likely a troff(1)
> input file, just as the keyword struct indicates a C program.  These tests are
> less reliable than the previous two groups, so they are performed last.


### Example: tricking detection

We will show how the language tests can be tricked to make a `python` script get
reported as a `ruby` script.

Create a file `test.py` with the following contents (note the blank first line):
```

"""
    module A
    end;
"""

print("hello world")
```

Run file and see it reported as `Ruby module source`
```
$ file test.py
test.py: Ruby module source, ASCII text
```

This is because the file matched a magic rule like the
following([reference][ruby]):
[ruby]:https://github.com/file/file/blob/c4c9192da7cc8dc7728f6520457a5d6200881905/magic/Magdir/ruby#L29-L32
```
!:mime  text/x-ruby
0 regex   \^[[:space:]]*(class|module)[[:space:]][A-Z]
>0  regex   (modul|includ)e\ [A-Z]|def\ [a-z]
>>&0  regex   \^[[:space:]]*end([[:space:]]+[;#].*)?$   Ruby script text
```

However it is most definitely a python script:
```
$python test.py
hello world
```

If we remove blank first line we will see it correctly reported as a `Python
script` because it now matches in that magic file at a higher strength
([reference][py]):
[py]:https://github.com/file/file/blob/c4c9192da7cc8dc7728f6520457a5d6200881905/magic/Magdir/python#L8-L9
```
# often the module starts with a multiline string
0 string/t  """ Python script text executable
```
