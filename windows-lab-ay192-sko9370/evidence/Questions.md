# Questions  


For each question you must also detail which tool you used to find the answer, and
what command line options or menu path (as applicable).  

Evidence File: `/DataLeakageCase/cfreds_2015_data_leakage_pc.dd`

## Registry and Logs (6)

- [ ]	What is the timezone setting? [registry]

The timezone setting is UTC - 3 hours.

This was found using FTK Imager to extract Registry Hive System (Root\Windows\System32\config\System). Then, the registry hives were viewable using Registry Explorer. Using the bookmarks menu, I could find the 'TimeZoneInformation' setting. The setting was set for a bias of 300. Microsoft documentation says that UTC = local time + bias. Then Local time = UTC - 300 bias = UTC - 3 hours. UTC-3 is commonly used by aviators or the military.

https://docs.microsoft.com/en-us/windows/desktop/api/timezoneapi/ns-timezoneapi-_time_zone_information

https://www.timeanddate.com/worldclock/timezone/papa

- [ ]	Who was the last user to logon into PC? [logs/registry]

The last user to log in was 'informant'.

FTK Imager was used to extract the Software registry hive. I used Registry Explorer to view the 'LastLoggedOnUser' from \SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI.

https://community.spiceworks.com/scripts/show/3414-windows-10-clear-last-logged-on-user

- [ ]	When was the last recorded shutdown date/time? [logs/registry]

The last recorded shutdown date/time was 2015-03-25 15:31:05.

In the SYSTEM registry hive, there is a bookmark called Windows. Under it, there is a setting called ShutdownTime in \SYSTEM\CurrentControlSet\Control\Windows. The data is in binary, however I saw a "Data Interpreter" in the lower right corner. Clicking this brought up a menu of a bunch of interpretations. The Windows FILETIME translation gave the most reasonable answer.

https://social.msdn.microsoft.com/Forums/en-US/cdf3c69e-f836-47e2-be86-0e6566d1bc5c/how-to-get-the-last-shutdown-time?forum=vcgeneral

- [ ]	What were the last three applications installed by the suspect? [registry]

I looked in 'HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall\[app name]' using registry explorer and listed items by most recent date and found these programs installed into a temporary folder for user Informant.

1. Microsoft .NET Framework 4 (similar instance installed twice)
2. Secure Data Removal for Windows (eraserInstallBootstrapper)
3. AppleCare Support (IXP374.TMP)

https://stackoverflow.com/questions/429738/detecting-installed-programs-via-registry/429810

## Execution (4)

The HR department wants solid evidence of the applications the suspect ran. [multi]  

- [ ] Fill out the following table for applications that were executed related
  to exfilling corporate data or hiding tracks. (benign example below)

| filename     | UserAssist | AppCompatCache | Prefetch | JumpList | LastDateTime             | FullPath |
|--------------|------------|----------------|----------|----------|--------------------------|----------|
| ping.exe     | No         | Yes            | Yes      | No       | 2015-03-25 14:58:34 (pf) | C:\Windows\SYSWOW64\ping.exe |
| SetupAdmin.exe |No|Yes |No|No| 2014-12-02 02:29:30 | C:\Users\INFORM~1\AppData\Local\Temp\IXP374.TMP\SetupAdmin.exe|
| clickonce_bootstrap.exe |No|Yes|No|No|2015-03-22 15:11:21 |C:\Users\informant\AppData\Local\Apps\2.0\AAEE5TR8.1PL\3ZO8K226.LA4\goog...app_86fd5b6b43e66935_0001.0003_02e0d8611226c884\clickonce_bootstrap.exe|
|googledrivesync.exe|Yes|Yes|Yes|No|2015-03-23 19:56:33|C:\Users\informant\Downloads\googledrivesync.exe|
|Eraser 6.2.0.2962.exe|Yes|Yes|Yes|No|2015-03-25 14:47:40|C:\Users\informant\Desktop\Download\Eraser 6.2.0.2962.exe|
|ccsetup504.exe|Yes|Yes|Yes|Yes|2015-03-25 14:48:28|C:\Users\informant\Desktop\Download\ccsetup504.exe|
|dotNetFx40_Full_setup.exe|Yes|Yes|Yes|No| 2015-03-25 14:50:15 |C:\Users\INFORM~1\AppData\Local\Temp\eraserInstallBootstrapper\dotNetFx40_Full_setup.exe|

UserAssist at Users\<user>\NTUSER.DAT\SYSTEM\ControlSet
https://www.forensicswiki.org/wiki/Windows_Registry
AppCompatCache bookmark in SYSTEM registry hive.
Prefetch at \Windows\Prefetch, exported from FTK Imager
https://searchenterprisedesktop.techtarget.com/definition/prefetch-folder-PF
JumpList at C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations & AutomaticDestinations.
https://www.forensicswiki.org/wiki/Jump_Lists
https://ericzimmerman.github.io/#!index.md
https://binaryforay.blogspot.com/2016/03/introducing-jlecmd.html


### hints

- A good registry tool is 'Registry Explorer' provided as a link on the desktop
  folder.  Registry Explorer has bookmarks to forensically relevant locations
  like 'UserAssist'.  Additionally, it will automatically do the ROT13 on
  'Count' entries.
- AppCompatCacheParser.exe or ShimCacheParser.py  
- JLECmd.exe for jump lists

## Users and Applications (20)

- [ ]	List the periods the suspect was logged on to the system. [logs]

Security Log, filter out only logon and logoff events
3/22/2015 10:34:24 AM - 10:38:15 AM
10:51:15 AM - 11:18:52 AM
11:19:42 AM - 11:28:28 AM
11:43:37 AM - 11:55:52 AM
11:55:57 AM - 11:56:58 AM
11:57:02 AM - 11:57:41 AM
11:57:54 AM - 12:00:08 AM

3/23/2015 1:24:24 PM - 5:02:53 PM
3/24/2015 9:21:36 AM - 5:07:25 PM
3/25/2015 6:15:35 AM - 11:30:57 AM


The HR department also needs confirmation of the e-mails that were sent and received by the suspect.

- [ ] List the date/time and subject of e-mails sent between the suspect and the 'spy'.

|Date/Time				|Sender		|Recipient	|Subject				|
|-----------------------|-----------|-----------|-----------------------|
|Tue 03/24/2015	17:05	|iaman		|spy		|Done					|
|Tue 03/24/2015	15:34	|iaman		|spy		|RE: Watch out!			|
|Tue 03/24/2015 15:32	|spy		|iaman		|Watch out!				|
|Tue 03/24/2015 09:35	|iaman		|spy		|RE: Last request		|
|Tue 03/24/2015 09:30	|iaman		|spy		|RE: Last request		|
|Tue 03/24/2015 09:25	|spy		|iaman		|Last request			|
|Mon 03/23/2015 16:41	|spy		|iaman		|RE: It's me			|
|Mon 03/23/2015 16:38	|iaman		|spy		|It's me				|
|Mon 03/23/2015 15:27	|iaman		|spy		|Re: Important request	|
|Mon 03/23/2015 15:26	|spy		|iaman		|Important Request		|
|Mon 03/23/2015 15:20	|spy		|iaman		|RE: Good job, buddy.	|
|Mon 03/23/2015 15:19	|iaman		|spy		|RE: Good job, buddy	|
|Mon 03/23/2015 15:15	|spy		|iaman		|Good job, buddy.		|
|Mon 03/23/2015 14:44	|iaman		|spy		|RE: Hello, Iaman		|
|Mon 03/23/2015 13:29	|spy		|iaman		|Hello Iaman			|

- [ ] What are the cloud services links that were provided to exfil data?

https://drive.google.com/file/d/0Bz0ye6gXtiZaVl8yVU5mWHlGbWc/view?usp=sharing

https://drive.google.com/file/d/0Bz0ye6gXtiZaakx6d3R3c0JmM1U/view?usp=sharing

- [ ] Find traces related to cloud services on PC [vss]  
    - [ ] export the three files related to Google Drive usage, include in the 'evidence' folder.
		1. snapshot.db
		2. sync_config.db
		3. sync_log.log
    - [ ] Identify account information for synchronizing Google Drive.
		Owner of google drive is 'Iaman Informant'. I clicked into the google drive link and looked at the details.
    - [ ] Use `sqlparser.py` (or another method) to identify two files that were shared via google drive.
		1. do_u_wanna_build_a_snowman.mp3
		2. happy_holiday.jpg
		
		I clicked into both google drive links and read the file name.

event logs in C:\WINDOWS\system32\config
https://searchwindowsserver.techtarget.com/definition/Windows-event-log

Outlook OST file in C:\Users\informant\AppData\Local\Microsoft\Outlook
Download Kernel OST Viewer to parse OST file.


### hints
- [Windows Logs Encyclopedia](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/Default.aspx)  
- [Logging cheat sheet] (https://www.malwarearchaeology.com/cheat-sheets/)  
- [Google Drive](http://forensicswiki.org/wiki/Google_Drive) Reference


## Windows Search database (15)

HR wants more evidence! Find the traces of e-mail communication stored in
Windows Search database.

- [ ] Export the system `Windows.ebd` ESE Database, include in 'evidence' folder.
		done
- [ ] The database table we are interested in is 'SystemIndex_0A', export this
  table with `esedbexport`. `$ esedbexport -l eselog.txt -t search -T 'SystemIndex_0A' <Windows.edb file>`

- [ ] Modify the included python script `searchESE.py` to print all e-mails to
  'spy.conspirator@nist.gov' included in the Windows Search database in
  a readable manner.
  
    https://docs.python.org/3/library/csv.html

- [ ] Dump the output of your python script to `evidence/spy_emails.txt`

	C:\python27-x64\python.exe ./searchESE.py -f .\SystemIndex_0A.7 -e 'spy.conspirator@nist.gov' > spy_emails.txt

- [ ] Did you find any additional evidence of e-mails not found in the Outlook file?

    Yes. An email from Mar 23 2015 18:44 says "Successfully secured."
    Then there is an email to spy containing 'space_and_earth.mp4' at Mar 23 2015 19:27.
    
### hints
- [Windows Desktop Search](http://forensicswiki.org/wiki/Windows_Desktop_Search)
  Reference 
- You may want to view the ESE database using the Nirsoft tool
  'ESEDatabaseView' for familiarity.

## Browser Activity (10)

Document browser activity related to anti-forensics and leaking sensitive information.

- [ ] Use the Nirsoft tool 'ChromeCacheView' to determine what PDF files the suspect downloaded.  

    User\informant\AppData\Local\Google\Chrome\User Data\Default\Cache
    
    DEFCON-20-Perklin-AntiForensics.pdf
    2001-leak_secret.pdf
    data-leakage-threats-mitigation-1931.pdf
    
- [ ] Use the Nirsoft tool 'ChromeHistoryView' to corroborate evidence of tools that were downloaded by the suspect.
    
    User\informant\AppData\Local\Google\Chrome\User Data\Default\History
    
    Outlook (email setup)
    Apple iCloud
    google Drive
    
### hints

- You will need to start the program as an Administrator and 'Select Cache Folder' from the File menu.  
- You will need to run as Administrator, and change the history file in the 'Advanced Options' menu.  
  