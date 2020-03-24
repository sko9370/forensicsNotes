# Questions

For each  of the following questions we provide the question, as well as the
expected answer. You are responsible for providing a command line, or script
that produces this answer.

For each question provide the command line or script that generates the answer,
in a separate file matching the following format.  `solve<Number>.sh`. Provide
any additional information, such as differences in format, or notes on what you
attempted in a single file named `errata.txt` with clear references to the
question.

## Using tcpdump and unix tools.

### Q1 (4)

In the file `/cases/lab3/q1.pcap` how many TCP sessions did `10.1.60.66`
initiate?

A1: `1866`

### Q2 (7)

In the file `/cases/lab3/q2.pcap` how many HTTP (GET or POST) requests came from
`10.1.60.68`?  

A2: `2276`

### Q3 (4)

In the file `/cases/lab3/q3.pcap` how many TCP packets transmitted to or from
10.1.60.67?  

A3: `58125`

### Q4 (10)

What are all the unique HTML titles in the file `/cases/lab3/q4.pcap`?  

A4: Find at least 102, see `a4.txt`.

#### Bonus (3)

Can you find even more (110)?

## Using tshark and unix tools.

### Q5 (5)

What are the top five 'talkers' by TCP conversation data transferred in the file
`/cases/lab3/q5.pcap`?  

A5: See the file `a5.txt`

### Q6 (5)

What IP address sent the most data in the file
 `/cases/lab3/q6.pcap`?  

A6: See the file `a6.txt`


### Q7 (10)

What files were transferred using SMB with source and destination IPs in the
file `/cases/lab3/q7.pcap`?

A7: See the file `a7.txt`
