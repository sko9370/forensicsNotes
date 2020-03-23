import csv, sys, argparse
from pprint import pprint
from textwrap import wrap

# C:\python27-x64\python.exe ./searchESE.py -f .\SystemIndex_0A.7 -e 'spy.conspirator@nist.gov' > spy_emails.txt

def searchESE(filename, email):
    with open(filename, 'rb') as csvfile:
        ese = csv.DictReader(csvfile, delimiter="\t")

        # System_Message_ToAddress
        # System_Message_DataSent
        # System_Message_DateReceived
        # System_Search_AutoSummary

        for row in ese:
            if row['System_Message_ToAddress'] == email:
                print(row['System_Message_ToAddress'], row['System_Message_DateReceived'], row['System_Search_AutoSummary'])		

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='ESE database export file (TSV format)')
    parser.add_argument('-e','--email', help='email address to search for')
    args = parser.parse_args()
    searchESE(args.file, args.email)

if __name__ == '__main__':
    main()
