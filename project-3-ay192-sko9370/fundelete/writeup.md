## fundelete

sleuthkit helps here.

I knew the flag was on a deleted file.
So I ran
"fls -rpd fundelete.fat" to find it.

Once I got the type of file and the inode it was assigned to, I ran
"icat 6 fundelete.fat > flag.jpeg" to output it to a file.

The flag was written on the jpeg image.
