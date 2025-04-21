#!/usr/bin/env python3

# usage: python3 choose.py k < list.tsv > output.tsv
#
# return all possible combinations of k elements from a given list, one per line
# the output is a tab separated list of couples, triples, quadruples, according to k


import sys

list = sys.stdin.read().splitlines()
list.sort()
k = int(sys.argv[1])

if k == 2:
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            print(list[i]+"\t"+list[j])

elif k == 3:
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            for l in range(j+1, len(list)):
                print(list[i]+"\t"+list[j]+"\t"+list[l])

elif k == 4:
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            for l in range(j+1, len(list)):
                for m in range(l+1, len(list)):
                    print(list[i]+"\t"+list[j]+"\t"+list[l]+"\t"+list[m])
