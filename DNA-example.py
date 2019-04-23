#!/usr/bin/env python3
"""
Author: Danielle Larson
Purpose: Output the reverse-complement of the given DNA strand
"""

import os
import sys
import argparse

# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Reverse complement the DNA strand',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('STR', help='DNA strand', type = str, metavar = 'STR')

    parser.add_argument(
        '-o',
        '--outfile',
        action='store',
        dest='outfile',
        help = 'File of the Reversed DNA strand',
        metavar = "FILE",
        default = "out.txt")

    parser.add_argument(
        '-d',
        '--DNA',
        action='store',
        required = True,
        dest='DNA',
        help = 'File with DNA strand',
        metavar = "FILE",
        default = "DNA.txt")    


    return parser.parse_args()
# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    outfile = args.outfile
    DNA = args.DNA

    if not os.path.isfile(DNA):
        die('"{}" is not a DNA strand'.format(DNA))

    output = ''

    with open("DNA.txt", "r") as f:
        DNA = f.readline()

        # print(DNA)

        for letter in DNA:
            if letter == 'A':
                output = 'T' + output
            elif letter == 'T':
                output = 'A' + output
            elif letter == 'C':
                output = 'G' + output
            elif letter == 'G':
                output == 'C' + output
            # print(output)

        with open(outfile, "w") as f:
            f.write(output)
            print('Output file written to "{}"'.format(outfile))



# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

    
# --------------------------------------------------
if __name__ == '__main__':
    main()