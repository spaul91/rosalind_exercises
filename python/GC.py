#!/usr/bin/env python3

import argparse

def parse_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--fasta", help="fasta file")

    args = parser.parse_args()

    return args

def calculate_gc(seq):
    gc_count = sum([base in ["G", "C"] for base in seq])
    return 100*float(gc_count / len(seq))

if __name__ == "__main__":

    args = parse_arguments()

    with open(args.fasta, "r") as f:
        names = []
        seqs = []
        this_sequence = ""
        for line in f:
            if line[0] != ">":
                this_sequence += line.rstrip()
            else:
                names.append(line.rstrip().lstrip(">"))
                if this_sequence != "":
                    seqs.append(this_sequence.strip())
                    this_sequence = ""
        seqs.append(this_sequence)

    gc_contents = [calculate_gc(seq) for seq in seqs]

    fasta_dict = dict(zip(names, gc_contents))

    max_gc_content = max(fasta_dict.values())

    max_gc_header = next(filter(lambda name: fasta_dict[name] == max_gc_content, fasta_dict))

    print(max_gc_header)
    print(round(max_gc_content, 6))
