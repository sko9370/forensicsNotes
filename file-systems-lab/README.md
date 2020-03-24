# File Systems and Carving Lab

## Admin

- Released: 1020, 28 Jan 2019
- Due: 1020, 04 Feb 2019
- Points: 35

## Lab Outcomes

1. Understanding file identification techniques.
2. The use of carving techniques to recover files.

## Lab Environment

- 10.4.83.XX
  - user: ubuntu
  - pass: ubuntu
- Same machine as lab 1.
- All files are in `/cases/lab2`

## File Identification

Given an unknown file, identify what type each file is and determine what
information the file may contain relevant to an investigation.  A good starting
point on a Unix system is the utility `file` which checks the file header (and
possibly other file data structures) against a known database.  

It is highly recommended that you read through included
[reference-file-command.md](./reference-file-command.md) document in order to
gain a better appreciation for your tools. The `file` command is just
a recommended starting point,  You are certainly not limited to just this one
command. Furthermore make sure you explain the meaning of the output rather than
just pasting it verbatim.

## File Carving 

### File carving with scalpel (SIFT)

An excerpt from the default "scalpel.conf" is provided with this Lab to use and
modify.  You can refer to the original found at `/etc/scalpel/scalpel.conf`.

### File carving with photorec (SIFT)

Photorec is an interactive tool with few command line options.

## Other References

- http://www.garykessler.net/library/file_sigs.html  
- http://mark0.net/soft-trid-deflist.html

