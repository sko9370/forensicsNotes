## Q1 (12)

### 1a. Offset (P) : 0x292dc28
command: python vol.py -f /cases/lab4/sample002.bin kdbgscan

### 1b. Most likely Profile: Win7SP1x86
X Win7SP1x86_23418	2016-04-09
X Win7SP1x86_24000	2018-01-09
O Win7SP1x86
X Win7SP0x86

1. stat /cases/lab4/sample002.bin
shows modified date is 2013-10-15
2. see Github source for profile dates to compare
3. test run psscan with remaining 2 profiles
python vol.py -f /cases/lab4/sample002.bin --cache --profile=Win7SP1x86 psscan
python vol.py -f /cases/lab4/sample002.bin --cache --profile=Win7SP0x86 psscan
4. they both work, so try verinfo to determine profile from executables
python vol.py -f /cases/lab4/sample002.bin --cache --profile=Win7SP1x86 verinfo
------------ --profile=Win7SP0x86 verinfo

both run and spit out a ton of output
however, the fileversion on both outputs mention win7sp1
therefore, the correct profile must be Win7SP1x86

### 1c. Cached Password Hashes
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Daniel:1000:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c:::

python vol.py -f /cases/lab4/sample002.bin --cache --profile=Win7SP1x86 hashdump

### 1d. User Daniel's password is 'password.'

https://crackstation.net

## Q2 (5)

### 2a. Which processes are active?

Active Processes
- alg.exe
- wuauclt.exe
- wscntfy.exe
- VMwareService.exe
- VMwareUser.exe
- VMwareTray.exe
- spoolsv.exe
- csrss.exe
- svchost.exe
- services.exe
- svchost.exe
- explorer.exe
- lsass.exe
- smss.exe
- winlogon.exe

1. Run kdbgscan to determine which profile to use for psscan and pslist
WinXPSP3x86
WinXPSP2x86

stat /cases/lab4/sample003.bin
modified 2010-12-16

python vol.py -f /cases/lab4/sample003.bin --cache kdbgscan

2. No luck with dates, try test run with psscan
both run fine

python vol.py -f /cases/lab4/sample003.bin --cache --profile=WinXPSP3x86 psscan
python vol.py -f /cases/lab4/sample003.bin --cache --profile=WinXPSP2x86 psscan

3. check verinfo
saw some with xpsp3, but most with xpsp
mostly sure it's WinXPSP3x86

python vol.py -f /cases/lab4/sample003.bin --cache --profile=WinXPSP3x86 verinfo
python vol.py -f /cases/lab4/sample003.bin --cache --profile=WinXPSP2x86 verinfo

xpsp.080413-2105 generally points to questions about xpsp3 on google

### 2b. cmd.exe exited at 2008-11-26 07:45:49 UTC+0000

### 2c. smss.exe is leftover from a previous reboot
python vol.py -f /cases/lab4/sample003.bin --cache --profile=WinXPSP3x86 pslist

## Q3 (5)

### 3a. Which process(es) are hidden?

'network_listener' is hidden from pslist and psscan
'svchost.exe'; 'cmd.exe'; 'services.exe'; 'alg.exe'; 'csrss.exe' are only hidden from pslist

python vol.py -f /cases/lab4/sample003.bin --cache --profile=WinXPSP3x86 psxview

### 3b. It attempted to hide by disabling discovery by pslist and psscan, but other plugins were still able to find it.

## Q4 (6) 

### 4a. There are 7 logged on Users. I looked at processes labeled "Logon Session" and counted every unique number after "S-1-5" because they are the revision number and identifier authority. I ran 'python vol.py -f /cases/lab4/sample005.bin --cache --profile=Win2003SP2x86 getsids | grep "Logon Session"'

1. Run kdbgscan to figure out correct profile to use
Win2003SP0x86
Win2003SP1x86
Win2003SP2x86
2. Check dates
modified 2012-11-27

stat /cases/lab4/sample005.bin

no dates available
3. Run psscan on profiles
python vol.py -f /cases/lab4/sample005.bin --cache --profile=Win2003SP0x86 psscan
X python vol.py -f /cases/lab4/sample005.bin --cache --profile=Win2003SP1x86 psscan
X python vol.py -f /cases/lab4/sample005.bin --cache --profile=Win2003SP2x86 psscan

Correct profile is Win2003SP0x86

### 4b. Administrators, Everyone, Authenticated Users, Users, Local Users, Local System, NT Authority, Local, This Organization, Performance Log Users, ssadmin, Domain users, Interactive, and Service.

python vol.py -f /cases/lab4/sample005.bin --cache --profile=Win2003SP0x86 getsids 
python vol.py -f /cases/lab4/sample005.bin --cache --profile=Win2003SP0x86 hivescan

### 4c. Yes, there seems to be very suspicious long SIDs associated with process 1928 for ssadmin and Domain users. Other processes similarly have very long SIDs that may be signs of privilege escalation.


## Q5 (3)

### 5a. System, smss.exe, csrss.exe, winlogon.exe, services.exe, lsass.exe, svchost.exe, spoolsv.exe, userinit.exe, explorer.exe, userinit.exe, reader_sl.exe, AdobeARM.exe, cmd.exe, mdd.exe (16 processes with 2 svchost.exe processes)

1. Run kdbgscan
WinXPSP3x86
WinXPSP2x86

2. just use WinXPSP3x86 since both work

python vol.py -f /cases/lab4/sample004.bin --profile=WinXPSP3x86 privs | grep 'Driver'
 

## Q6 (3)

### 6a. There are 13 variants of the Zeus virus running.

python vol.py zeusscan2 --plugins=/home/ubuntu/volatility-2.6.1/community/ZeusScan/ -f /cases/lab4/sample006.bin --cache --profile=WinXPSP3x86 | grep Process | sort -u | wc -l

## Q7 (21)

### 7a. Process 1096 is accessing the ")!VoqA.I4" mutex.

python vol.py -f /cases/lab4/sample004.bin --profile=WinXPSP3x86 handles | grep ')!VoqA.I4'
0x821422b8	1096	0x2f0	0x1f0001	Mutant	)!VoqA.I4

### 7b. It's categorized as a mutant type, which means it might be malformed.

### 7c. The password for this malware is 'tigers'

python vol.py poisonivyscan --plugins=/home/ubuntu/volatility-2.6.1/community/AndreasSchuster/ -f /cases/lab4/sample004.bin --cache --profile=WinXPSP3x86
same but with poisonivyconfig

### 7d. The version number is 231.

### 7e. There were 2 active connections

python vol.py -f /cases/lab4/sample004.bin --profile=WinXPSP3x86 connections 

### 7f. It accessed host-190.iad3.verisign.com, host-190.lax2.verisign.com, and softbank221054197032.bbtec.net.

python vol.py -f /cases/lab4/sample004.bin --profile=WinXPSP3x86 connscan | grep ':80'
python vol.py -f /cases/lab4/sample004.bin --profile=WinXPSP3x86 connscan | grep ':443'
host 199.7.59.190
host 199.7.52.190
host 221.54.197.32

### 7g. No, RDP uses port 3389, which was not used recently.

python vol.py -f /cases/lab4/sample004.bin --profile=WinXPSP3x86 connscan | grep ':3389'

## Q8. Bonus (10 points)

### 8a. Yes, csrss.exe, services.exe, svchost.exe, explorer.exe, lsass.exe.

python vol.py -f /cases/lab4/sample007.bin --cache --profile=WinXPSP3x86 ldrmodules
python vol.py -f /cases/lab4/sample007.bin --cache --profile=WinXPSP3x86 malfind | grep Process

python vol.py -f /cases/lab4/sample007.bin --cache kdbgscan
WinXPSP2x86
WinXPSP3x86

X python vol.py -f /cases/lab4/sample007.bin --cache --profile=WinXPSP2x86 psscan # and verinfo
python vol.py -f /cases/lab4/sample007.bin --cache --profile=WinXPSP3x86 psscan # and verinfo

### 8b. Yes, lsass.exe, both PID 1928 and 868.

python vol.py hollowfind --plugins=/home/ubuntu/volatility-2.6.1/community/MonnappaKa -f /cases/lab4/sample007.bin --cache --profile=WinXPSP3x86 

### 8c. The files are named sample007_malfind and sample007_hollowfind.

### 8d. The rootkit works by hooking IRP functions.

python vol.py -f /cases/lab4/sample007.bin --cache --profile=WinXPSP3x86 devicetree
python vol.py -f /cases/lab4/sample007.bin --cache --profile=WinXPSP3x86 driverirp

### 8e. 

python vol.py -f /cases/lab4/sample007.bin --cache --profile=WinXPSP3x86 driverscan 

### 8f. Yes, these kernel modules show up as DLLs because they are officially recognized by the OS as signed.

python vol.py -f /cases/lab4/sample007.bin --cache --profile=WinXPSP3x86 moddump --dump-dir /cases/lab4/sample007_moddump
file * | grep DLL

### 8g. Yes, there are GenericKernelCallbacks, KeBugCheckCallbackListHeads, and KeRegisterBugCheckReasonCallback.

python vol.py -f /cases/lab4/sample007.bin --cache --profile=WinXPSP3x86 callbacks | grep Callback
