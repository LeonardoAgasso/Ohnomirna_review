import sys
import requests

def retrieve_sequence(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text.strip().split('\n', 1)[1].replace('\n', '')
    else:
        return None

def retrieve_sequences_from_bed():
    for line in sys.stdin:
        bed_line = line.strip().split('\t')
        chrom, start, end, _, header_info = bed_line[:5]
        api_url = f"http://togows.org/api/ucsc/hg38/{chrom}:{start}-{end}.fasta"
        sequence = retrieve_sequence(api_url)
        if sequence:
            header = f">{chrom}:{start}-{end}_{header_info}"
            print(header)
            print(sequence)

retrieve_sequences_from_bed()