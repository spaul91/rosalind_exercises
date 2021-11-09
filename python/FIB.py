#!/usr/bin/env python3

import argparse

def parse_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--months", help="months", type=int)
    parser.add_argument("-k", "--litter_size", help="litter size", type=int)

    args = parser.parse_args()

    return args.months, args.litter_size

def g(k):
    def f(n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return f(n - 1) + f(n - 2)*k
    return f

if __name__ == "__main__":

    n, k = parse_arguments()

    f = g(k)

    for i in range(1, n+1):
        print(f(i))
