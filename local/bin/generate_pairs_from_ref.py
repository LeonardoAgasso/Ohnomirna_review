#!/usr/bin/env python3

import sys
import itertools

def get_subgenome(index):
    if index in [0, 1]:
        return 'one'
    elif index in [2, 3]:
        return 'two'
    else:
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <prefix>")
        sys.exit(1)

    prefix = sys.argv[1]

    # Read from stdin
    lines = [line.strip() for line in sys.stdin if line.strip()]

    # Skip header
    header = lines[0].lstrip('#').split('\t')
    data_lines = lines[1:]

    print("miRNA_1\tmiRNA_2\tWGD\tclg")
    
    for line in data_lines:
        fields = line.split('\t')
        mirnas = fields[0:4]
        clg = fields[6]

        # Collect present miRNAs with their subgenome
        present = [(mirna, get_subgenome(i)) for i, mirna in enumerate(mirnas) if mirna != "absent_loc"]

        # Generate all unique pairs
        for (mirna1, sub1), (mirna2, sub2) in itertools.combinations(present, 2):
            relation = "2R" if sub1 == sub2 else "1R"
            print(f"{prefix}-{mirna1}\t{prefix}-{mirna2}\t{relation}\t{clg}")

if __name__ == "__main__":
    main()