# Windows Artifacts Lab

## Admin

- Released: 1020, 26 Mar 2019
- Due: 1020, 8 Apr 2019
- Points: 55

## Lab Outcomes

1. Demonstrate the extraction and analysis of Windows Artifacts, including from
   the registry and to demonstrate evidence of execution.
2. Familiarity with the use of multiple tools to understand a system.

## Lab Environment

- Virtual Machines: https://vcsa1.eecs.net
- Data: `\\cs483-wsrv\cases`
  - `DataLeakageCase/cfreds_2015_data_leakage_pc.dd`

## Refrences

Tools
- [RegRipper](https://github.com/keydet89/RegRipper2.8)
- [shellbags.py](https://github.com/williballenthin/shellbags)
- [ShimCacheParser](https://github.com/mandiant/ShimCacheParser)

Documentation
- [About the Registry](https://docs.microsoft.com/en-us/windows/desktop/SysInfo/about-the-registry)
- [Advanced Registry](https://support.microsoft.com/en-us/help/256986/windows-registry-information-for-advanced-users)

## Scenario  

‘Iaman Informant’ was working as a manager of the technology development
division at a famous international company OOO that developed state-of-the-art
technologies and gadgets. One day, at a place which ‘Mr. Informant’ visited on
business, he received an offer from ‘Spy Conspirator’ to leak of sensitive
information related to the newest technology. Actually, ‘Mr. Conspirator’ was an
employee of a rival company, and ‘Mr. Informant’ decided to accept the offer for
large amounts of money, and began establishing a detailed leakage plan.  

‘Mr. Informant’ made a deliberate effort to hide the leakage plan. He discussed
it with ‘Mr. Conspirator’ using an e-mail service like a business relationship.
He also sent samples of confidential information though personal   cloud
storage.  

After receiving the sample data, ‘Mr. Conspirator’ asked for the direct delivery
of storage devices that stored the remaining (large amounts of) data.
Eventually, ‘Mr. Informant’ tried to take his storage devices away, but he   and
his devices were detected at the security checkpoint of the company.  And he was
suspected of leaking the company data.  

At the security checkpoint, although his devices (a USB memory stick and a CD)
were briefly checked (protected with portable write blockers), there was no
evidence of any leakage. And then, they were immediately transferred to  the
digital forensics laboratory for further analysis.  

The information security policies in the company include the following:  
1.  Confidential electronic files should be stored and kept in the authorized 
    external storage devices and the secured network drives.  
2.  Confidential paper documents and electronic files can be accessed only 
    within the allowed time range from 10:00 AM to 16:00 PM with the appropriate 
    permissions.  
3.  Non-authorized electronic devices such as laptops, portable storages, 
    and smart devices cannot be carried onto the company.  
4.  All employees are required to pass through the ‘Security Checkpoint’ system.  
5.  All storage devices such as HDD, SSD, USB memory stick, and CD/DVD are 
    forbidden under the ‘Security Checkpoint’ rules.  

In addition, although the company managed separate internal and external
networks and used DRM (Digital Rights Management) / DLP (Data Loss Prevention)
solutions for their information security, ‘Mr. Informant’ had sufficient
authority to bypass them. He was also very interested in IT (Information
Technology), and had a slight knowledge of digital forensics.  
