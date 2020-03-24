# Questions

Answer the following questions in `Answers.md`.

When necessary be sure to include the command line that you ran to determine the
answer. If you used config files be sure to include those files (clearly named)
as well.

## Q1 (12)

Analyze `sample002.bin`.

- 1a. What is the KDBG offset for this image?

- 1b. What is the most likely correct profile to use?

- 1c. Extract the cached password hashes (using `hashdump`) on sample002.bin.

- 1d. Load them into a password cracker to determine the plain text password (if
possible). At least one password can be cracked.

## Q2 (5)

Run the `pslist` and `psscan` plugins against `sample003.bin`. (ch5)

- 2a. Which process(es) are active (list executable names)?

- 2b. Which process(es) have terminated? 

- 2c. Which process(es) are leftover from a previous reboot?

## Q3 (5)

Run the `psxview` plugin against `sample003.bin`. (ch6)  

- 3a. Which process(es) are hidden?

- 3b. In what ways did the rootkit attempt to hide?

## Q4 (6)

Run the `getsids` plugin against `sample005.bin`. (ch6)

- 4a. How many users are logged on? How did you determine logged on users?

- 4b. What are their names?

- 4c. Is there any evidence of privilege escalation attacks?

## Q5 (3)

Run the `privs` plugin against `sample004.bin`. (ch6)

- 5a. In `sample004.bin`, which process(es) have the ability to load kernel drivers?

## Q6 (6)

Run the `zeusscan2` plugin against `sample006.bin`. (ch7)

This requires a community plugin. Follow the [instructions](running-plugins.md)
to analyze this sample.

- 6a. How many unique variants of Zeus are running?  What makes a variant unique?

## Q7 (18)

Analyze `sample004.bin`.

Run the `handles` plugin against `sample004.bin`? (ch6)

- 7a. Which process is currently accessing the `")!VoqA.I4"` mutex?   

- 7b. What is the significance of this mutex?

Based on your analysis, there's one community plugin created to analyze this
malware. Use the PID from 7a.

- 7c. What is the password for this malware C2?

- 7d. What is the version number?

Run `connections` and `connscan` plugins on `sample004.bin`.

- 7e.  How many active connections did sample004.bin have? 

- 7f.  What websites (port 80 or 443) did it access in the recent past? 

- 7g.  Was RDP enabled on `sample004.bin`?  (ch11)

## Q8. Bonus (10 points)

Analyze `sample007.bin` (use plugins `ldrmodules`, `malfind`, `hollowfind` ).  (ch8)

- 8a. Are any processes hosting injected code? If so, which one(s)?

- 8b. Have any processes been hollowed? If so, which one(s)?

- 8c. Extract the injected code segments or hollowed process executable to
disk for further static analysis.

Analyze `sample007.bin` (use plugins `devicetree`, `driverirp`, `callbacks`, `driverscan`, `moddump`):

- 8d. Does this rootkit work by hooking IRP functions or using layered devices?

- 8e. What functionality or capabilities can you uncover?

- 8f. Are any of the kernel modules digitally signed?

- 8g. Does the rootkit install any callbacks or timers?

