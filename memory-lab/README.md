# Memory Analysis LAB

## Admin

- Released: 1020, 21 Feb 2019
- Due: 1020, 4 MAR 2019
- Points: 55

## Lab Outcomes

1. Given memory captures determine the answers to forensically relevant
   questions.
2. Familiarity with the volatility memory forensics framework

## Lab Environment

- 10.4.83.XX
  - user: ubuntu
  - pass: ubuntu
- Same machine as previous labs.
- All files are in `/cases/lab4`
- All chapter references refer to the chapters in *Art of Memory Forensics*.


## Background

Memory forensics can provide a wealth of information about the current state of
the system. From processes information, to files, and network connections,
almost everything passes through memory. With the increasing prevalence of
memory-resident or fileless malware, sometimes memory analysis is the only
mechanism for discovering malicious activity.

The `volatility` [framework][v] is:

> a completely open collection of tools, implemented in Python under the GNU
> General Public License, for the extraction of digital artifacts from volatile
> memory (RAM) samples.  The extraction techniques are performed completely
> independent of the system being investigated but offer visibility into the
> runtime state of the system. The framework is intended to introduce people to
> the techniques and complexities associated with extracting digital artifacts
> from volatile memory samples and provide a platform for further work into this
> exciting area of research.

In this lab we will provide memory artifacts and you will use a series of
`volatility` plugins to gain information for further analysis. You will also
gain exposure to community provided plugins which greatly add to the utility of
the framework.

[v]:https://github.com/volatilityfoundation/volatility
