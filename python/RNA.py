#!/usr/bin/env python3

from DNA import parse_arguments

def transcribe_rna(dna_string):
    rna = dna_string.replace("T", "U")
    return rna

if __name__ == "__main__":

    args = parse_arguments()

    with open(args.input, "r") as f:
        dna = f.read().strip()
        print(transcribe_rna(dna))
