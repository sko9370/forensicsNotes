## chimera

The hint says to mount it.
It gives me an error right away because it can't figure out what the type of filesystem it is.
This makes sense because it's a "chimera."
I didn't know the correct options flag for it and which filesystems I was choosing from.

Turns out I should've read the error. Actually read it.
It tells me what command to use, "wipefs," but I didn't even try it because I thought it would 'wipe' something from the image.

I have to choose between ext2 or fat. Easy enough.
I can mount it and browse to a keypart. What are all the fill files? random junk
I'm surprised I can mount it as both filesystems....

I initially thought that the image was super special and that the same bytes were able to be viewed in ext2 and fat.
But nothing is that coincidental. Turns out the 'keypart' in ext2 and fat are completely different.

I asked CPT Ragsdale about this and he mentioned one of the older problems mentioning xor'ing two parts.
Bingo, chimeras are blended parts of 2 different animals.

I extracted the two keyparts using icat and xor'ed them together. This resulting file had the flag.
