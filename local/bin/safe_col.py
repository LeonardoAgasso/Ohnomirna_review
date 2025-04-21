#!/usr/bin/env python3

import sys
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Replace spaces with underscores in a specific column from STDIN."
    )
    parser.add_argument("column", type=int, help="1-based column number to modify")
    parser.add_argument("-s", "--sep", default='\t', help="Field separator (default: tab)")

    args = parser.parse_args()

    column_index = args.column - 1
    if column_index < 0:
        print("Error: COLUMN must be a positive integer", file=sys.stderr)
        sys.exit(1)

    for line in sys.stdin:
        parts = line.rstrip('\n').split(args.sep)
        if column_index < len(parts):
            parts[column_index] = parts[column_index].replace(' ', '_')
        print(args.sep.join(parts))

if __name__ == '__main__':
    main()