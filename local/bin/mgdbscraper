#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sys

url = "https://mirgenedb.org/browse/hsa"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table')

if table:
    rows = []
    for row in table.find_all('tr'):
        row_data = [cell.get_text() for cell in row.find_all('td')]
        rows.append(row_data)
else:
    print("No table found in the HTML.")

rows = [row[:16] for row in rows]

rows = rows[3:]

for row in rows:
    for i in range(len(row)):
        row[i] = row[i].replace("\n", "")

# In the last three columns, substitute empty strings with "0"
for row in rows:
    for i in range(13, 16):
        if row[i] == " ":
            row[i] = "0"

header = ['#MirGeneDB_ID', 'MirBase_ID', 'Family', 'Seed', '5p_acccession', '3p_accession', 'Chromosome', 'Start', 'End', 'Strand', 'Node_of_origin_(locus)', 'Node_of_origin_(family)', '3\'_NTU', 'UG_motif', 'UGUG_motif', 'CNNC_motif']

# print the header and the rows to the standard output
print("\t".join(header))
for row in rows:
	print("\t".join(row))
