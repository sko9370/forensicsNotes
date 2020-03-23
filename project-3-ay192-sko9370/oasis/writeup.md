## oasis

What is this rhythm business in the hint?

I tried using strings and filtering the nonsense but it turns out there were way too many.

sleuthkit helped here.
I used fls to find that inode 12 contained the flag somehow.
Using debugfs, I read the data of inode 12 using mi <12>.
I saw that direct block addresses were super high, so just went through blkcat'ing the direct listed blocks blkcat 2715 had the flag.
