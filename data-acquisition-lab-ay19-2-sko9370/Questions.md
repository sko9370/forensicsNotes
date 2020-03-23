# Questions

For each of these questions provide the answer in a file named for the question
in the following format `a<Question Number><Question Part>.txt` (e.g.
`a2c.txt`).

1. Using the vsphere web console take a snapshot of the machine. Provide the
   snapshot name (3).

2. For each of the following, provide the answer, the command line that you
   used to capture the information and a sha256 hash of the collected data. (3 each).
    - a. Date and time
    - b. Active network connections
    - c. Routing table
    - d. IP address
    - e. Users
    - f. Disk partition information

3. Retrieve the Master Boot Record from `/dev/sda` using `dd`, submit as
   `a3.mbr.data` ensure you also provide a hash of this collected data. (5)

4. Capture two other pieces of forensically relevant information. Record what
   you captured, how you captured it (command line), the data, hash, and  why it
   is forensically relevant. (2 each)

## Bonus (3)

5. Provide a listing of the sha256 hashes for all the binaries in `/usr/bin` in
   a file named `usr_bin.sha256`. Provide the hash of this file and the command
   line used to collect it in `a5.txt`
