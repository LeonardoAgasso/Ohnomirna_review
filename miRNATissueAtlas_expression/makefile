.DELETE_ON_ERROR:

hsa_mirgenedb3.0_to_everything.tsv:
	ln -s ../0_miRNA_parsing/$@ ./$@

mature_to_mgdb.dic: hsa_mirgenedb3.0_to_everything.tsv
	cat $< | awk -F"\t" '{print $$14"\t"$$1}' | sort | uniq > $@

all_human_miRNA_rpmm_harmonized_meta_data.mgdb.csv: mature_to_mgdb.dic
	cat all_human_miRNA_rpmm_harmonized_meta_data.csv | awk -F"\t" 'NR>5' | translate -a -d -j -v -e unknown_mirna $< 1 | cut -f1 --complement | sort | uniq > $@.noheader;
	cat all_human_miRNA_rpmm_harmonized_meta_data.csv | awk -F"\t" 'NR>1 && NR<=5' > header;
	cat header $@.noheader | strip_mirna_name 1 > $@;
	rm $@.noheader header