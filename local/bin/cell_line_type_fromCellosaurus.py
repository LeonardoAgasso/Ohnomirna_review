#!/usr/bin/env/python3

import sys
from Bio.ExPASy import cellosaurus

with open('cellosaurus.txt') as handle:
    records = cellosaurus.parse(handle)
    for record in records:
        print(record['ID']+'\t'+record['CA'])