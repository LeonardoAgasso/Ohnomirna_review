#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import combinations

def get_prefix(name):
    parts = name.split('-')
    return '-'.join(parts[:3]) if len(parts) >= 3 else name

def find_paralog_pairs(mirna_list):
    groups = defaultdict(list)
    for mirna in mirna_list:
        prefix = get_prefix(mirna)
        groups[prefix].append(mirna)

    pairs = []
    for group in groups.values():
        if len(group) > 1:
            pairs.extend(combinations(group, 2))

    return pairs

def main():
    mirnas = [line.strip() for line in sys.stdin if line.strip()]
    pairs = find_paralog_pairs(mirnas)

    for pair in pairs:
        print(f"{pair[0]}\t{pair[1]}")

if __name__ == "__main__":
    main()