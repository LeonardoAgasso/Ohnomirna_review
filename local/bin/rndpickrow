#!/usr/bin/env python3

import sys
import random
import argparse

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Pick N rows at random from a file.")
    parser.add_argument("N", type=int, help="Number of random rows to pick.")
    args = parser.parse_args()
    n = args.N

    # Read file from standard input
    input_lines = sys.stdin.readlines()
    
    # Validate N
    if n > len(input_lines):
        print("Error: N is greater than the number of rows in the file.", file=sys.stderr)
        sys.exit(1)

    # Pick N random rows
    random_rows = random.sample(input_lines, n)

    # Output the random rows
    for row in random_rows:
        print(row, end='')

if __name__ == "__main__":
    main()
