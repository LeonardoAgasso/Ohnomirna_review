#!/usr/bin/env python3

import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_mirna_origin_info(mirna_name):
    try:
        species_code, mirna_id = mirna_name.split("-", 1)
        species_code = species_code.lower()
        url = f"https://mirgenedb.org/show/{species_code}/{mirna_id}"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        results = {
            "Node of Origin (locus)": None,
            "Node of Origin (family)": None
        }

        for row in soup.find_all("tr"):
            header = row.find("th")
            data = row.find("td")
            if header and data:
                label = header.get_text(strip=True)
                value = data.get_text(strip=True)
                if label in results:
                    results[label] = value

        return results["Node of Origin (locus)"] or "NA", results["Node of Origin (family)"] or "NA"

    except Exception:
        return "NA", "NA"

def main():
    if len(sys.argv) != 2:
        print("Usage: append_mirgenedb_info.py <miRNA_column_number>", file=sys.stderr)
        sys.exit(1)

    try:
        col_index = int(sys.argv[1]) - 1
    except ValueError:
        print("Error: Column number must be an integer.", file=sys.stderr)
        sys.exit(1)

    for line in sys.stdin:
        line = line.rstrip("\n")
        if not line.strip():
            print(line)
            continue

        fields = line.split("\t")

        if col_index < 0 or col_index >= len(fields):
            print(f"{line}\tNA\tNA", file=sys.stderr)
            continue

        mirna = fields[col_index]
        locus, family = get_mirna_origin_info(mirna)
        print(f"{line}\t{locus}\t{family}")

if __name__ == "__main__":
    main()