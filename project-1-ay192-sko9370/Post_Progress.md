# Post Progress

## Progress so Far

The original plan was to improve upon cuishark, which is a terminal-based app that looks like top but works for wireshark.
However, I've had immense difficulty even getting it to run in a Linux environment.
I suspect that there is just something wrong with the base c files with libcuishark, which is the c wrapper around wireshark that the author uses.
I've sinced abandoned that route.

I've instead taken my original goal of implementing tab completion for tshark to make it more user-friendly for general usage.
Since I'm most familiar with python, I started researching terminal-based app development libraries.
I know curses and ncurses were the gold standard, but within the time constraint, that would have been difficult to flesh out.
Instead, I found a short tutorial on a basic python tutorial on developing a terminal app. It only used one library.

http://introtopython.org/terminal_apps.html#What-are-terminal-apps?

Using the 'clear' shell command to make it seem as though the shell wasn't scrolling was genious and blew my mind.
I didn't need ncurses to make a seemingly interactive and dynamic terminal app.

I initially thought that I could just take user input and run the tshark command using the 'os' library just like how the tutorial did for 'clear'
That quickly became a problem.
First, how to get the output of that command and print it. The answer was actually just to use the subprocess library.
Second, how would I ever implement tab completion?
Before I got to answer that one, I found pyshark, a python wrapper around most commands in wireshark.
It was stable, it worked, and I could make it work.
It was definitely a bit limited than what I originally planned but it could print out full packet info and use display filters.

Now I got to the point where I could have the user choose to print out the entire pcap packet summaries, print out a specific packet's info, use a filter, or quit.
I needed to improve the option to use a filter so that the user could type a letter, press tab, and then see the correct suggestions below.
That's when I found the readline library.

https://pymotw.com/2/readline/

This link had the example code that implemented tab completion and suggestion. Good find.

## Next Steps

The most recent kink was that tab completion somehow bled over into the main menu, not just the filter entry.
I need to somehow isolate that or implement tab completion for the main menu too, possibly every menu.

Once tab completion is fixed, I need to add in the entire list of filters available to wireshark.
Wireshark has a reference page for all of it, but I may need to filter through and pick out the most commonly used. It's a lot.
Then I can have python read them in by text file.

Extending upon the last step is to provide a format for arguments.
Once a certain filter parameter is chosen, the correct format for that particular filter parameter should be somehow displayed.
Maybe not as a tab suggestion, but a popup or prompt example (i.e. ip.addr==10.10.45.1).

That would be the hardest step.
Polishing this app would include making sure pyshark/tshark doesn't break because a couple times, it froze when I ran commands quickly after one other.
The appearance could also always use polish.
I can't add color as it stands, but I can add more ascii spacing and art.
Adding in the ability to see livecapture results is also an option.
I started with that functionality but found it hard to implement.
I may try again now that I have a greater understanding of the simple libraries I found.

## Try it Out

A prototype of the app is available in the repo as 'wire.py'
I've been wondering what to call it, maybe WirePy??
Not sure, there are a lot of modules and libraries out there that play on the word wireshark and they're all so different.
I may need to differentiate mine a bit more.

To run 'wire.py', you need to run a bit of setup.
1. must use python3
2. sudo apt install tshark
3. sudo dpkg-common configure wireshark (say yes)
4. sudo chmod +x /usr/bin/dumpcap (might not be necessary)
5. sudo setcap cap_net_raw,cap_net_admin+eip /usr/sbin/tcpdump (also might not be necessary)
6. pip3 install pyshark

'python3 wire.py' will do

Try it out and send me any feedback.
I'm working on this on and off so any guidance to save me time for me is greatly appreciated.

psst, I'm keeping my working repo hidden.
