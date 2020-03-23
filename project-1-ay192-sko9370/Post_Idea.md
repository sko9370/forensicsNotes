# Interactive TShark
A reactive commandline app that makes it easy and pleasant to analyze live traffic or saved pcap files.

## Motivation
The CS483 Network lab was hard.
tcpdump was a dump and even tshark was hard to use because of how many different options there were.
The number of times I troubleshooted the perfect filter or correct option usage was ridiculous.
There must be an easier way to analyze packets without losing focus on a specific packet and what you're typing.

I've used wireshark in at least 3 different classes for a variety of applications.
There's plenty of reason to expand upon its capabilities, especially in a restricted environment.

An example of a restricted environment for tools is limiting usage to the command line.
That got me thinking about the "top" command in linux.
It's purely on the command line, but it's dynamic and updates values in real time.
It also features many many different aspects of system status details.
Think processor usage, free memory, up time, and process details.

What if I could build something like that for Wireshark?

To my disappointment, cuishark (linked below) does exactly what I pictured.
But I investigate the repo and it's pretty lacking in features and polish.

First, it's coded in Go, which isn't as popular as python or other languages.
Second, all commands are typed at the bottom of the screen, much like vim.
This makes it a bit more difficult to use, in my opinion.
Vim was not friendly to people like me.
There's also a disturbing lack of color that I'm used to seeing in the wireshark GUI.
The readme's also needed much clarification, extension, and correction.

Maybe there is enough for me to do here...

## Problem Statement
Create a reactive commandline app that...
- tab-completes filter keywords
- explains relevant value meanings

Non-Vital
- uses python so that more people can contribute features to it or customize it to their liking
- has a colored search bar that turns green and red to indicate the correctness of the filter.
- supports Windows

## Plan
My contribution will be to add more features to include greater color usage and filter suggestions.
Additionally, the original contributor is not an native English speaker so the readme's should be updated.
I believe this project will benefit from a python implementation, but more thought needs to go into changing the entire structure.
Lastly, a stretch goal would be to have Windows support for the app.
The Wireshark GUI is available on several types of distributions and to be truly usable, the CUI should also be made equally versatile.

### Structure
The backend is a C library called libcuishark that was already created by the same person that created cuishark.
It builds off of libwireshark, which is usually not meant for general usage because it is not well documented.
The frontend will utilize python or Go (depending on architecture choice) to display on the commandline.
A possible consequence of implementing Windows support may mean the backend may become python as well.

### Challenges
The biggest challenge I see is figuring out how exactly to make the search bar dynamic.
That way, each new key will search through a list of filters to return suggestions on words and values.

The second biggest challenge is how to provide the list of filters and values.
In Wireshark, when you start to type in a filter, suggestions come up very quickly.

Additionally, the expression wizard shows options for the different values some filters can be set to.
The different values are defined, making it easier to figure out which bit/number value is the correct one to use.
Getting this list of values and making them available for queries in conjunction with the filter keywords will be difficult.

Understanding what has already been done will be difficult because I'm not familiar with Go.
The balance between starting from scratch in python vs learning Go and extending the project will be close.
The decision needs to be made early on, however.

### So what?
I'm planning on improving a command line implementation of wireshark to make it even more user friendly.
It will be more fun to use than tshark or tcpdump without the bog that comes with a full GUI.
My end goal will be to make the network lab trivial with the use of this tool.

### Prior Works and References
- [nethog](https://github.com/raboof/nethogs)
	- lightweight program similar to "top" that tracks which processes are transferring the most packets
	- useful as a monitoring tool to make sure no unwanted information is going out
- [libcuishark](https://github.com/cuishark/libcuishark)
	- c wrapper library of wireshark used by cuishark
- [cuishark](https://github.com/cuishark/cuishark)
	- command line implementation of wireshark
	- could use more features and polish
