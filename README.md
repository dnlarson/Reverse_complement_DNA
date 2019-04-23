# Reverse_complement_DNA
Find the reverse complement of the given DNA strand (ROSALIND SOLUTION)

Nucleic acids are long, chain-like molecules that express one's genetic information. Each nucleic acid contains four of the five bases: Adenine (A), Guanine (G), Cytosine (C), Thymine (T), and Uracil (U). Thymine (T) is found in DNA, while Uracil (U) is found in RNA. In this problem we will be focusing on DNA's complementary pairs: A and T, C and G.

In this problem, you will use import argparse to read in a file called DNA.txt and find the complement of each base in the provided DNA string and reverse it (i.e. "GTCA" is "TGAC"). The output will be written to a default file called "out.txt".

# Expected Behavior
The DNA string and outfile are both required, so be sure to set `required=True` when creating it with `parser.add_argument` so the program makes a usage statement when no arguments are provided:

````
$ ./DNA-example.py 
usage: DNA-example.py [-h] [-o FILE] -d FILE
DNA-example.py: error: the following arguments are required: -d/--DNA
````

Create help page on `-h` or `--help`:

````
$ ./DNA-example.py -h
usage: DNA-example.py [-h] [-o FILE] -d FILE

Reverse complement the DNA strand

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --outfile FILE
                        File of the Reversed DNA strand (default: out.txt)
  -d FILE, --DNA FILE   File with DNA strand (default: DNA.txt)
  ````
  Die when wrong file argument is given:
  
  ````
  ./DNA-example.py -d foo
  "foo" is not a DNA strand
  ````
  # Expected Output
  
  
  Contact:
  Danielle Larson
  (dnlarson@email.arizona.edu)
  
  
  
