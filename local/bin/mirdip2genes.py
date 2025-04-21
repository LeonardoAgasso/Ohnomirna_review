#!/usr/bin/env python3

import sys
import pandas as pd




def main():
	file = sys.stdin
	df = pd.read_csv(file, sep="\t", header=None)
	df.columns = ["miRNA", "Gene", "Score"]

	# Score is in the format +2.10738457410390E-001 when miRNA and Gene are the same keep the one with the highest score
	df = df.sort_values(by="Score", ascending=False)
	df = df.drop_duplicates(subset=["miRNA", "Gene"], keep="first")

	# print the file as stdout sorted by score
	df.to_csv(sys.stdout, sep="\t", header=False, index=False)


if __name__ == "__main__":
	main()
