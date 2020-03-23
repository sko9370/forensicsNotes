## Summary
Named WirePy, the python app is an interactive commandline tool used to analyze pcap files.
It is a departure from what was originally planned because the program that I initially planned on improving was glitchy and just did not work well enough to warrant any improvement.
I still tried to implement tab completion, which was the main point of my initial plan, with varying success.
The current implementation provides a simple interactive method of analyzing small to medium size pcap files without requiring a GUI.

## Status
The app is working as expected and users will get the results they are supposed to.
Work remains to be done with improving the tab completion feature.

## Usage
To run 'wire.py', you need to run a bit of setup.
 1. must use python3
 2. sudo apt install tshark
 3. sudo dpkg-common configure wireshark (say yes)
 4. sudo chmod +x /usr/bin/dumpcap (might not be necessary)
 5. sudo setcap cap_net_raw,cap_net_admin+eip /usr/sbin/tcpdump (also might not be necessary)
 6. pip3 install pyshark

Now that we're done with the setup, use 'python3 wire.py' to start the app.

The very first screen will present you with a prompt asking for the name of the pcap file.
You must provide the exact name of the pcap file, which must be located in the same directory.
Use the provided "test.pcap" if you want to follow along.

Pressing enter brings up a menu that allows you to choose whether...
- you want to view a summarized list of all the packets
- you want to input a specific filter
- you want to examine a specific packet
- you want to quit for some reason

A summarized list of packets provides a traversable list of one-line packet descriptions (thanks to 'less').

If you want to use a filter, you are given two more choices (so many choices).
You can either type in a wshark format filter or type in a text filter (grep).
The wshark format filter will run the filter into pyshark (python's wrapper over tshark).
This was originally where the tab completion was meant to be fully fleshed out.
However, as it is, only a couple options show up after pressing tab twice.
They are some options like "ip.addr" or "ip.src" that would be used in wshark filters.
The text filter will utilize grep to filter through the complete packet list to match any part of a packet.
This caters to users that are unfamiliar with wshark filter format or those that have a very specific search criteria.
If you wanted to search for something contained in the data portion of a packet, conventional wshark filters would not work.

If you want to examine a specific packet, you must provide a packet number.
These are available on either of the previous options.
Choosing a specific packet will display the complete description, including all its different layers.

At any point, the output is saved to "pcaptemp" in the same directory that allows the output to be "less"ed through.
However, this also serves the purpose of allowing the user to quit at any time and save the file for access at a later time.
This makes piping or complicated commandline-fu less necessary for non-time-intensive operations.

You may move back and forth between any of these options as the menus will loop continuously until you quit.

## Future Work
There is lots of room for improvement and polish.
Primarily, the tab completion feature is incompletely implemented as is.
I've demonstrated part of its functionality, but it is not feasible to continue developing it with the current setup of the menus.
The way I have step-by-step inputs makes it difficult to use tab completion because I need to create separate classes for each of them.
If rather I reduce the number of separate menus, I think tab completion will become easier to flesh out.
The matter of what to tab complete is difficult, though.
Wireshark has a reference page of all the arguments and parameters.
I thought about copying that text over and reading that in through python to use as a list reference for filters.
However, I got caught up in getting tab completion to work properly between menus that that never came to be.

Another point of improvement could be caching of some sort.
A medium sized pcap takes a couple seconds to parse through and display.
But reading that same pcap file over and over again would take the same amount of time, even though it's showing the same details.
Maybe keeping separate temp files between the options and then keeping track of which commands were run so that pyshark doesn't have to run every time.
Ideally, pyshark would only be run once through the whole thing and the other options will be much faster to run.

## Success?
It's lacking to call this a complete success in reference to the original goal.
Actually it's not even close.
Someone famous said even a good plan doesn't survive first contact with the enemy.
The enemy here was time, learning curve, and too-optimistic goal-setting.
