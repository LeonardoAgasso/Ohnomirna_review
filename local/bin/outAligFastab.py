#!/usr/bin/env python3

# This script converts a FASTA file to a TSV file

import sys

rows = []
current_row = []


def findDist(word1, word2, symbols):
	
	# seq1 and seq2 have the same length, check the first index such that seq1[i] = seq2[i]
	for i, (char1, char2) in enumerate(zip(word1, word2)):
		if char1 == char2:
			index1 = i

	# check the index such that the string symbols[index] = "|"
	for i, char in enumerate(symbols):
		if char == "|":
			index2 = i

	# return the distance between the two indexes
	return index1 - index2

def fixSymbols(word1, word2):
	if len(word1) != len(word2):
		raise ValueError("Input words must have the same length")

	comparison_string = ""
	for char1, char2 in zip(word1, word2):
		if char1 == '-' or char2 == '-':
			comparison_string += ' '
		elif char1.upper() == char2.upper():
			comparison_string += '|'
		else:
			comparison_string += '.'

	return comparison_string


for line in sys.stdin:
	
	line = line.strip()

	if line.startswith(">"):

		if current_row:
			rows.append(current_row)

		current_row = [line]
	else:
		current_row.append(line)

if current_row:
	rows.append(current_row)

for row in rows:
	#strip the ">" from the first element of the list
	row[0] = row[0][1:]

	# retrieve from the first element of the list the first word and save it as "name1"
	name1 = row[0].split()[0]
	name2 = row[0].split()[3]

	score = row[4][6:]

	name1 = name1.replace(":", "")
	name2 = name2.replace(":", "")

	#n = findDist(row[1].upper(), row[3].upper(), row[2])
	fixed_symbols = fixSymbols(row[1], row[3])

	print(row[0] + "\t" + row[1] + "\t"  + fixed_symbols + "\t" + row[3] + "\t" + row[4]  + "\t" + score + "\t" + name1 + "\t" + name2)
	
