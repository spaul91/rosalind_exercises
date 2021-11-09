#!/usr/bin/env python3

import argparse

def parse_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", help="input file")

    args = parser.parse_args()

    return args

def increment_count(counts, base):
    counts[base] += 1
    return counts

def count_bases(dna_string):
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}
    list(map(lambda pos: increment_count(counts, pos), dna_string))
    return(counts)

if __name__ == "__main__":

    args = parse_arguments()

    counts = {"A": 0, "C": 0, "G": 0, "T": 0}

    with open(args.input, "r") as f:
        dna = f.read().strip()
        counts = count_bases(dna)
        print(f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}") 
