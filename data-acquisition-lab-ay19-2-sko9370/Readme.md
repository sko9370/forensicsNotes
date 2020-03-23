# Lab 1: Data Acquisition

This lab provides a familiarization with the process of a live response and data
acquisition with minimal tools.


## Admin

- Released: 1020, 22 Jan 2019
- Due: 1020, 28 Jan 2019
- Points: 30


## Lab Outcomes

1. Familiarity with virtualized environment, eecsNet, and lab expectations.
2. Demonstrated ability to acquire artifacts from a live system including the
   necessary validation data.
3. Experience with Linux command line tools and the ability to look up command
   syntax and usage.

## Lab Environment

- https://vcsa1.eecs.net
- lab1.<LAST_NAME>.cs483
  - user: ubuntu
  - pass: ubuntu

## Example

This is an example of a series of commands and how they might be used to
forensically acquire information from a live system.

#### command

`netstat` 


#### manual

```
$ man netstat
NETSTAT(8)                                         Linux System Administrator's Manual                                         NETSTAT(8)

NAME
       netstat - Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships
```

#### usage (standard out)

```
$ netstat -an
```

- `-a`, `--all`
  - "Show both listening and non-listening sockets"
- `-n`, `--numeric`
  - "Show numerical addresses instead of trying to determine symbolic host, port
    or user names."

#### output to a file


```
$ netstat -an > netstat.txt
```

#### output to stdout and file

```
$ netstat -an | tee netstat.txt
```

#### output to stdout/file and hash output

```
$ netstat -an | tee netstat.txt | sha1sum
```

#### output to stdout/file and save hashes

```
$ netstat -an | tee netstat.txt | sha1sum > netstat.sha1
```


## Simple Remote Data Collection

Often you will need to retrieve data from a remote machine (in this case the
victim machine which is being analyzed). Here are two ways that can be achieved.

#### python HTTP Server

On the victim machine:

```
python3 -m http.server
```

On your analysis machine:

wget http://<VICTIM_IP>:8000/<FILE_NAME>


#### netcat

From your analysis/collection machine:

```
$ nc -l -p 46400 | tee netstat.txt | sha1sum > netstat.sha1
```

In words, start a server listening on port 46400, output the results
to both `netstat.txt` and `stdout`, taking the sha1 hash of `stdout` and stave
that as `netstat.sha1`

From the victim machine.

```
$ netstat -an | nc -w 3 <ANALYSIS_MACHINE_IP> 46400
```

In words, run the `netstat` command and output the resulting data over the
netcat connection to the analysis machine on port 46400.
