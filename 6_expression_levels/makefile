.DELETE_ON_ERROR:

SPECIES := hsa

hsa-tissueItems.txt:
	wget -O$@ 'https://mirgenedb.org/static/data/$(SPECIES)/$(SPECIES)-tissueItems.txt'

hsa-tissueItems.tsv: hsa-tissueItems.txt
	sed 's/,/\t/g' $< > $@