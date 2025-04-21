#!/usr/bin/env python3

import sys
import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser(description="Filter rows based on column presence in external file.")
    parser.add_argument("-i", nargs='+', type=int, required=True, help="Columns to check (1-based index).")
    parser.add_argument("-f", type=int, required=True, help="Column in filter file to use (1-based index).")
    parser.add_argument("-s", default='\t', help="Field separator (default: tab).")
    parser.add_argument("filter_file", help="Path to the file containing allowed values.")
    return parser.parse_args()

def clean_suffix(value):
    # Remove suffixes like "_pre", "-v1_pre", "-v10_pre" (case insensitive)
    return re.sub(r'(-v\d+)?_pre$', '', value, flags=re.IGNORECASE)

def load_filter_values(filter_file, col_index, sep):
    with open(filter_file, 'r') as f:
        return set(
            clean_suffix(line.strip().split(sep)[col_index])
            for line in f if line.strip()
        )

def main():
    args = parse_args()

    check_cols = [i - 1 for i in args.i]  # Convert to 0-based index
    filter_col = args.f - 1
    sep = args.s

    allowed_values = load_filter_values(args.filter_file, filter_col, sep)

    for line in sys.stdin:
        line = line.rstrip('\n')
        if not line:
            continue
        fields = line.split(sep)

        try:
            values_to_check = [fields[i] for i in check_cols]
        except IndexError:
            continue  # skip malformed lines

        if all(val in allowed_values for val in values_to_check):
            print(line)

if __name__ == "__main__":
    main()