# Questions

For the following files, answer these three questions:

a. What type of file is this?

b. How did you determine and confirm the file type?

c. What relevant information does this file contain?

For each file provide the answers the answers to these questions in a file
named `a<Number>.txt`. Be sure to include commands run, the output, as well as
your detailed explanation.

# File identification (4 each)

1. /cases/lab2/file001
2. /cases/lab2/file002
3. /cases/lab2/file003
4. /cases/lab2/file004

# File carving

Use the identified tools to perform file carving on: `/cases/lab2/carve001`

## With scalpel  (5)

Run scalpel with the default configuration file provided, and provide your
answers in a single file `a5.txt`.

`$ scalpel -o scalpel-default -O -c scalpel.conf /cases/lab2/carve001`   

5. `scalpel`

  a. How many of each type of file were recovered?   
  
  b. How many of the recovered files are valid?  
  
  c. Why do you think scalpel recovers invalid files?

## With photorec (5)

Run photorec with the default search and provide your answers in a single file
`a6.txt`.

`$ photorec /d photorec-default /cases/lab2/carve001`

Select "Proceed", "Search", "Other", and "Quit", "Quit", "Quit"  

6. `photorec`

  a. How many of each type of file were recovered?
  
  b. How many of the recovered files are valid?
  
  c. How does photorec work. What principles does it use and rely on?

## Validation (4)

Provide the sha256 hashes of all files recovered with each technique:

- `scalpel.sha256`
- `photorec.sha256`

## Compare (5)

7. Compare the results from scalpel and photorec.  Why did one tool perform
   better than the other? Answer in `a7.txt`

# Bonus (3)

Create a file that is recognized one way by `file` but is actually some other
format, or works validly as both.  Provide the contents of the file in `bonus`
and the explanation in `bonux.txt`. You may not use the same technique as the
provided example.
