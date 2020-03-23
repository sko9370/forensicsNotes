#!/usr/bin/env/python3

# http://introtopython.org/terminal_apps.html#What-are-terminal-apps?
# much thanks to this guide for helping me build a terminal app

import os
from time import sleep
from subprocess import Popen, PIPE
import pyshark
import readline
import logging

LOG_FILENAME = './completer.log'
logging.basicConfig(filename=LOG_FILENAME,
            level=logging.DEBUG,
            )

class BufferAwareCompleter(object):

    def __init__(self, options):
        self.options = options
        self.current_candidates = []
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            # first time for this text, so build a match list

            origline = readline.get_line_buffer()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            being_completed = origline[begin:end]
            words = origline.split()

            logging.debug('origline=%s', repr(origline))
            logging.debug('begin=%s', begin)
            logging.debug('end=%s', end)
            logging.debug('being_completed=%s', being_completed)
            logging.debug('words=%s', words)

            if not words:
                self.current_candidates = sorted(self.options.keys())
            else:
                try:
                    if begin == 0:
                        # first words
                        candidates = self.options.keys()
                    else:
                        # later word
                        first = words[0]
                        candidates = self.options[first]

                    if being_completed:
                        # match options with portion of input
                        # being completed
                        self.current_candidates = [ w for w in candidates
                                                if w.startswith(being_completed) ]

                    else:
                        # matching empty string so use all candidates
                        self.current_candidates = candidates

                    logging.debug('candidates=%s', self.current_candidates)

                except ((KeyError, IndexError), err):
                    logging.error('completion error: %s', err)
                    self.current_candidates = []

        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        logging.debug('complete(%s, %s) => %s', repr(text), state, response)
        return response

def input_loop():
    readline.parse_and_bind('tab: complete')
    line = ''
    oldLine = ''
    while line != 'stop':
        oldLine = line
        line = input('type in your filter and press tab to autocomplete: ')
        if line != '':
            confirm = input("is \"%s\" okay, y or n? " % line)
            if confirm == 'y':
                return oldLine
            else:
                pass
    return line

readline.set_completer(BufferAwareCompleter(
    {'ip.addr':[],
    'ip.src':[],
    'ip.dst':[],
    'tcp.ack':[],
    'tcp.port':[],
    'stop':[],
     }).complete)

### Title Bar ###

def display_title():
    os.system('clear')

    print("\t****************WirePy****************")

### User Input ###

def get_pcap_name():
    pcapName = input("pcap file name? ")

    return pcapName

def get_user_input():
    print("\n")
    print("[1] see everything")
    print("[2] choose a filter")
    print("[3] examine a packet in detail")
    print("[q] quit")
    print("\n")

    return input("well, what's your choice? ")

### Main Program ###

choice = ''
display_title()
pcapName = get_pcap_name()

while choice != 'q':

    choice = get_user_input()

    display_title()

    if choice == '1': # see everything
        # https://www.saltycrane.com/blog/2008/09/how-get-stdout-and-stderr-using-python
        # -subprocess-module/

        print("\nyou chose 1!\n")
        pcap = pyshark.FileCapture(pcapName, only_summaries=True)
        # for packet in pcap:
            # print(packet)
        output = open("pcaptemp", "w")
        for packet in pcap:
            output.write(str(packet) + "\n")
        os.system('less pcaptemp')
        output.close()

    elif choice == '2': # choose a filter
        print("\nyou chose 2!\n")

        print("\ndo you want to type in a wshark filter or a text filter?\n")

        answer = ""
        while answer != "w" and answer != "t":
            answer = str(input("[w]shark or [t]ext: "))
            if answer != "w" and answer != "t":
                print("that's not one of the choices, try again\n")

        if answer == "w":
            # possibly import list of all display-filter keywords to list from file
            # check filter input to this list of words to help correct user input
            validFilters = []

            # filters = input("filters here (like 'http and ip.addr==10.10.4.251') ")
            filters = input_loop()

            # allow for a couple seconds of delay
            print("\nplease wait a few seconds\n")
            pcap = pyshark.FileCapture(pcapName,
                    display_filter=filters,
                    only_summaries=True)
            output = open("pcaptemp", "w")
            for packet in pcap:
                output.write(str(packet) + "\n")
            os.system('less pcaptemp')
            output.close()

        elif answer == "t":
            full = ""
            while full != "t" and full != "s":
                full = str(input("scan through full [t]ext (this takes a while) or [s]ummary? "))
                if full != "t" and full != "s":
                    print("that's not one of the choices, try again")
            summary = True
            if full == "t":
                summary = False

            textFilter = str(input("enter your text filter here (i.e.: TCP 73): "))
            print("\nplease wait a few seconds\n")
            pcap = pyshark.FileCapture(pcapName,
                    only_summaries=summary)
            output = open("pcaptemp", "w")
            for packet in pcap:
                if textFilter in str(packet):
                    output.write(str(packet) + "\n")
            # os.system("cat pcaptemp | grep \"%s\" | less" % textFilter)
            os.system("cat pcaptemp | less")
            output.close()

    elif choice == '3': # examine a packet in detail
        print("\nyou chose 3!\n")
        packetNumber = int(input("packet number: "))

        # allow for a couple seconds of delay
        print("\nplease wait a few seconds\n")
        pcap = pyshark.FileCapture(pcapName)
        print(pcap[packetNumber])

    elif choice == 'q': # quit
        print("\nyou chose to quit\n")
        print("\nleaving\n")

    else:
        print("\nnot valid choice, try again\n")
