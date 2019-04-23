# Reverse_complement_DNA
Find the reverse complement of the given DNA strand (ROSALIND SOLUTION)

Nucleic acids are long, chain-like molecules that express one's genetic information. Each nucleic acid contains four of the five bases: Adenine (A), Guanine (G), Cytosine (C), Thymine (T), and Uracil (U). Thymine (T) is found in DNA, while Uracil (U) is found in RNA. In this problem we will be focusing on DNA's complementary pairs: A and T, C and G.

In this problem, you will use `import argparse` to read in a file called DNA.txt and find the complement of each base in the provided DNA string and reverse it (i.e. "GTCA" is "TGAC"). The output will be written to a default file called "out.txt".

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
$ ./DNA-example.py -d foo
"foo" is not a DNA strand
````
Note: To start off with a smaller section of the given string, you can view the first 20 characters in DNA.txt by using
```` 
$ command | cut -c1-20 DNA.txt
GTCTGCCCCTAGACCAGTAA
````
# Expected Output
````  
$ ./DNA-example.py -d DNA.txt
Output file written to "out.txt"
$ cat out.txt
CCAAGTTTAGATGGGCCGAAAAATTTCGCCCGTGATTGCCGGAACTTTAGGAACAAATGCAGTTCAGGTAGGTCA
TGAATGAGTGGTAGGTAATACTTCACTTCAGGGACGCACGCCCGGATTGTGCAGAACGTACCGCTTGCAAACGGT
GGGCTGAAAACGTCAGCTGATTACATCATCCATCCGTTTAGAACTTAAACATTGGTCGTCGTAATTCTTAACCTG
GTCGGGCCAAATGTCCAAACGTCGCTCGACGCACTGACATCACATCTTTAATCCAAGTATAATTCTTAGCCAACG
GTTCCAAAAGTGTACGCCGCCCATGTGATGCAATGCGTGGTTTTTCGACCGAGGCGTTCTTTAACACAGTTTAGC
TCAAACTAATGCTGGGCATGGGACGCATTTTCAGAAGTGGTTTGAGTTTGAAAGTCGCTCTTACTGACGTACTGC
TGAAGGGGATTAATACCTTAATTACACTCTGTTCATTAAAAGTCTGGATGTAGATTGCTTCCCGGCAGAAATGTC
CGGGTAGCCTGAGATACCCTTACTCACGACGCAGCGATGAAACGTGCGTTCTATTAAAAAGTACACCCGGCCCGA
CTTGGTCCACGGCATATCAAACAGTAGCAGTCATGCCGATCTAGGATGAGTGGGACGGCTACAGTGTTTAAGGAA
TATTCCTACGCTGGTGGATGAGCTGCCTTCCTCCGGCTCATAAAGAGCAATCGGAGAGAGGCACATCAACTAACG
AGCGGCCCCTGGTAGGAACCAGAAGAGTTCAACCGGGTCGCACGGCCGGCTATCATCAGGCTCCAATCTATCTAC
CCTCCTCTGATGAGCTACATTTCCGAAGTTCCCGAGGGTTTCCGCTCGTATCACTTAAGGAGATGTGAATTTACT
GGTCTAGGGGCAGAC
````

# Test Suite
Passing tests should look like:
````
$ make test
python3 -m pytest -v test.py
=================================================== test session starts ===================================================
platform darwin -- Python 3.7.0, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
cachedir: .pytest_cache
rootdir: /Users/daniellelarson/Reverse_complement_DNA, inifile:
collected 3 items                                                                                                         

test.py::test_usage PASSED                                                                                          [ 33%]
test.py::test_bad_args PASSED                                                                                       [ 66%]
test.py::test_good_input PASSED                                                                                     [100%]

================================================ 3 passed in 1.02 seconds =================================================
````  

Contact:
Danielle Larson
(dnlarson@email.arizona.edu)
  
  
  
