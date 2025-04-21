#!/usr/bin/env python3

import sys

def main():
    header = None
    seq_lines = []

    for line in sys.stdin:
        line = line.strip()
        if line.startswith('>'):
            if header:
                print(f"{header}\t{''.join(seq_lines)}")
            header = line[1:]  # remove '>'
            seq_lines = []
        else:
            seq_lines.append(line)

    # Print the last entry
    if header:
        print(f"{header}\t{''.join(seq_lines)}")

if __name__ == '__main__':
    main()