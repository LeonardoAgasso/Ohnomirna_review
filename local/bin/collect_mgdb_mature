#!/usr/bin/env python3

import sys
import re

def parse_args():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} MATURE_MIRNA_LIST", file=sys.stderr)
        sys.exit(1)
    return sys.argv[1]

def clean_mature_name(mature_name):
    # Remove suffixes like _3p, _5p, _3p*, _5p*
    return re.sub(r'(_[35]p\*?)$', '', mature_name)

def load_mature_miRNAs(filename):
    mature_map = {}
    with open(filename) as f:
        for line in f:
            name = line.strip()
            key = clean_mature_name(name)
            mature_map.setdefault(key, []).append(name)
    return mature_map

def main():
    mature_file = parse_args()
    mature_map = load_mature_miRNAs(mature_file)

    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        pre1, pre2 = parts
        matures1 = mature_map.get(pre1, [])
        matures2 = mature_map.get(pre2, [])
        for m1 in matures1:
            for m2 in matures2:
                print(f"{m1}\t{m2}")

if __name__ == '__main__':
    main()