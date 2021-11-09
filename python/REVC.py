#!/usr/bin/env python3

from DNA import parse_arguments

def reverse_complement(dna):
    comp_lookup = {"A": "T", "T": "A", "G": "C", "C": "G"}
    rev_dna = dna[::-1]
    trans_table = rev_dna.maketrans(comp_lookup)
    reverse_comp = rev_dna.translate(trans_table)
    return reverse_comp

if __name__ == "__main__":

    args = parse_arguments()

    with open(args.input, "r") as f:
        dna = f.read().strip()
        print(reverse_complement(dna))
