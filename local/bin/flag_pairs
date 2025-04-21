#!/usr/bin/env python3

import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Flag rows in FILE_1 based on presence of column pairs in FILE_2.")
    parser.add_argument("-l", "--label", default="present", help="Label to add when the pair is found in FILE_2.")
    parser.add_argument("-e", "--else-label", default=None, help="Label to add when the pair is NOT found in FILE_2.")
    parser.add_argument("--both-orders", action="store_true", help="Treat pairs as unordered.")
    parser.add_argument("col1_file1", type=int, help="1-based column index from FILE_1 (first element of pair).")
    parser.add_argument("col2_file1", type=int, help="1-based column index from FILE_1 (second element of pair).")
    parser.add_argument("file2", type=str, help="Path to FILE_2.")
    parser.add_argument("col1_file2", type=int, help="1-based column index from FILE_2 (first element of pair).")
    parser.add_argument("col2_file2", type=int, help="1-based column index from FILE_2 (second element of pair).")
    return parser.parse_args()

def load_pairs(file_path, col1, col2, both_orders=False):
    pair_set = set()
    with open(file_path) as f:
        for line in f:
            fields = line.rstrip('\n').split('\t')
            if col1 > len(fields) or col2 > len(fields):
                continue  # skip malformed lines
            a, b = fields[col1 - 1], fields[col2 - 1]
            if both_orders:
                pair_set.add(tuple(sorted((a, b))))
            else:
                pair_set.add((a, b))
    return pair_set

def main():
    args = parse_args()

    file2_pairs = load_pairs(
        args.file2,
        args.col1_file2,
        args.col2_file2,
        both_orders=args.both_orders
    )

    for line in sys.stdin:
        fields = line.rstrip('\n').split('\t')
        if args.col1_file1 > len(fields) or args.col2_file1 > len(fields):
            sys.stdout.write(line.rstrip('\n') + '\t' + (args.else_label or '') + '\n')
            continue
        a, b = fields[args.col1_file1 - 1], fields[args.col2_file1 - 1]
        key = tuple(sorted((a, b))) if args.both_orders else (a, b)
        if key in file2_pairs:
            label = args.label
        else:
            label = args.else_label or ''
        sys.stdout.write(line.rstrip('\n') + '\t' + label + '\n')

if __name__ == "__main__":
    main()