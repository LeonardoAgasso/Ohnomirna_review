.DELETE_ON_ERROR:


# =====================================================================
#                         VARIABLES
# =====================================================================
MIRGENEDB_VERSION := 3.0
GENCODE_RELEASE := 47
SPECIES := hsa
MIRGENEDB_GFF_URL := https://mirgenedb.org/
ENSEMBL_URL := http://www.ensembl.org/biomart/martservice
MIRBASE_DOWNLOAD_URL := https://mirbase.org/download/
# =====================================================================


# Downloads from mirbase.org + parsing
miRNA.dat:
	wget '$(MIRBASE_DOWNLOAD_URL)miRNA.dat'

hairpin.fa:
	wget '$(MIRBASE_DOWNLOAD_URL)hairpin.fa'

mature.fa:
	wget '$(MIRBASE_DOWNLOAD_URL)mature.fa'


primirna.sequence.tsv: miRNA.dat
	mir_emblparser.py < $< > $@

maturemirna.sequence.tsv: mature.fa
	mir_fastaparser.py < $< | awk -F"\t" '{print $$1"\t"$$3}' > $@




# Downloads from mirgenedb.org + parsing
mirgenedb$(MIRGENEDB_VERSION)_$(SPECIES).precursor_sequence.fa:
	wget -O$@ '$(MIRGENEDB_GFF_URL)fasta/$(SPECIES)?pre=1'

mirgenedb$(MIRGENEDB_VERSION)_$(SPECIES).precursor_sequence_wflanks.fa:
	wget -O$@ '$(MIRGENEDB_GFF_URL)fasta/$(SPECIES)?pri=1'

mirgenedb$(MIRGENEDB_VERSION)_$(SPECIES).mature_sequence.fa:
	wget -O$@ '$(MIRGENEDB_GFF_URL)fasta/$(SPECIES)?mat=1'

mirgenedb$(MIRGENEDB_VERSION)_$(SPECIES).star_sequence.fa:
	wget -O$@ '$(MIRGENEDB_GFF_URL)fasta/$(SPECIES)?star=1'

mirgenedb$(MIRGENEDB_VERSION)_$(SPECIES).5p_mature_sequence.fa:
	wget -O$@ '$(MIRGENEDB_GFF_URL)fasta/$(SPECIES)?prime=5'

mirgenedb$(MIRGENEDB_VERSION)_$(SPECIES).3p_mature_sequence.fa:
	wget -O$@ '$(MIRGENEDB_GFF_URL)fasta/$(SPECIES)?prime=3'

mirgenedb$(MIRGENEDB_VERSION)_$(SPECIES).loop_sequence.fa:
	wget -O$@ '$(MIRGENEDB_GFF_URL)fasta/$(SPECIES)?loop=1'


mirgenedb$(MIRGENEDB_VERSION)_$(SPECIES).%.tsv: mirgenedb$(MIRGENEDB_VERSION)_$(SPECIES).%.fa
	cat $< | fasta_to_tab > $@

