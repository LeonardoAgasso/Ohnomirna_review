#!/usr/bin/env python3
import sys
import re

def clean_mirna_name(name):
    # Remove _pri _pre and -vN_pre (case-insensitive)
    return re.sub(r'(-v\d+)?_pre$|_pri$', '', name, flags=re.IGNORECASE)

def main():
    if len(sys.argv) != 2:
        print("Usage: strip_mirna_name.py <column_number>")
        sys.exit(1)

    try:
        col_index = int(sys.argv[1]) - 1  # convert to 0-based
    except ValueError:
        print("Column number must be an integer.")
        sys.exit(1)

    for line in sys.stdin:
        line = line.rstrip('\n')
        if not line.strip():
            continue
        fields = line.split('\t')
        if col_index >= len(fields):
            print(line)  # keep line as-is if column index is out of bounds
            continue
        fields[col_index] = clean_mirna_name(fields[col_index])
        print('\t'.join(fields))

if __name__ == "__main__":
    main()