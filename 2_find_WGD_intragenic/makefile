.DELETE_ON_ERROR:

ORG_CAP := Hsa
ORG := hsa

ohnomirna_pairs_predict_$(ORG_CAP)_existent.names.extended_info.tsv:
	ln -s ../1_retrieve_Hsa_ohnomirnas/$@ ./$@

%.gene_pairs.name.tsv:
	ln -s ../../OhnomiRNAs/dataset/gene_pairs/$@ ./$@

gencode.protein_coding_genes.bed:
	ln -s ../0_miRNA_parsing/$@ ./$@

mgdb_3_$(ORG).premirna.tsv:
	ln -s ../1_retrieve_Hsa_ohnomirnas/$@ ./$@

mgdb_3_$(ORG).premirna.bed: mgdb_3_$(ORG).premirna.tsv
	cat $< | awk -F"\t" '{print $$1"\t"$$4"\t"$$5"\t"$$9"\t"$$7"\t"$$10}' | sort | uniq > $@

mgdb_3_$(ORG).premirna.host_gene.bed: mgdb_3_$(ORG).premirna.bed gencode.protein_coding_genes.bed
	bedtools intersect -wb -a $(word 1, $^) -b $(word 2, $^) > $@

mgdb_3_$(ORG).premirna.host_gene.compact.tsv: mgdb_3_$(ORG).premirna.host_gene.bed
	cat $< | awk -F"\t" '{print $$4"\t"$$6"\t"$$10"\t"$$14}' | sort | uniq > $@

mgdb_3_$(ORG).premirna.host_gene.compact.strip_mirna_name.dic: mgdb_3_$(ORG).premirna.host_gene.compact.tsv
	cat $< | strip_mirna_name 1 > $@

ohnomirna_pairs_predict_$(ORG_CAP)_existent.names.extended_info.host_genes.tsv: ohnomirna_pairs_predict_$(ORG_CAP)_existent.names.extended_info.tsv mgdb_3_$(ORG).premirna.host_gene.compact.strip_mirna_name.dic
	cat $(word 1, $^) | awk -F"\t" 'NR>1' | translate -a -d -j -v -e intergenic $(word 2, $^) 1 | translate -a -d -j -v -e intergenic $(word 2, $^) 9 | sort | uniq > tmp1;
	cat tmp1 | cut -f2,10 --complement | awk -F"\t" '{print $$1"\t"$$4"\t"$$5"\t"$$6"\t"$$7"\t"$$3"\t"$$2"\t"$$8"\t"$$11"\t"$$12"\t"$$13"\t"$$14"\t"$$10"\t"$$9"\t"$$15"\t"$$16}' | sort | uniq > tmp2;
	echo "#MiRGeneDB_name_1\tgene_ID_1\tgene_name_1\tmirbase_premirna_accession_1\ttranscript_name_1\thost_gene_name_1\thost_gene_ID_1\tMiRGeneDB_name_2\tgene_ID_2\tgene_name_2\tmirbase_premirna_accession_2\ttranscript_name_2\thost_gene_name_2\thost_gene_ID_2\tWGD\tCLG" >> $@;
	cat tmp2 >> $@;
	rm tmp*

ohnomirna_pairs_predict_$(ORG_CAP)_existent.names.extended_info.flagged_WGD_host_genes.tsv: ohnomirna_pairs_predict_$(ORG_CAP)_existent.names.extended_info.host_genes.tsv ohnologs.gene_pairs.name.tsv
	cat $(word 1, $^) | awk -F"\t" 'NR>1' | flag_pairs -l WGD --both-orders -e not_related 6 13 $(word 2, $^) 1 2 | sort | uniq > tmp1;
	echo "#MiRGeneDB_name_1\tgene_ID_1\tgene_name_1\tmirbase_premirna_accession_1\ttranscript_name_1\thost_gene_name_1\thost_gene_ID_1\tMiRGeneDB_name_2\tgene_ID_2\tgene_name_2\tmirbase_premirna_accession_2\ttranscript_name_2\thost_gene_name_2\thost_gene_ID_2\tWGD\tCLG\thost_genes_homology" >> $@;
	cat tmp1 >> $@;
	rm tmp*

ohnomirna_pairs_predict_$(ORG_CAP)_existent.names.extended_info.flagged_SSD_host_genes.tsv: ohnomirna_pairs_predict_$(ORG_CAP)_existent.names.extended_info.host_genes.tsv paralogs.gene_pairs.name.tsv
	cat $(word 1, $^) | awk -F"\t" 'NR>1' | flag_pairs -l SSD --both-orders -e not_related 6 13 $(word 2, $^) 1 2 | sort | uniq > tmp1;
	echo "#MiRGeneDB_name_1\tgene_ID_1\tgene_name_1\tmirbase_premirna_accession_1\ttranscript_name_1\thost_gene_name_1\thost_gene_ID_1\tMiRGeneDB_name_2\tgene_ID_2\tgene_name_2\tmirbase_premirna_accession_2\ttranscript_name_2\thost_gene_name_2\thost_gene_ID_2\tWGD\tCLG\thost_genes_homology" >> $@;
	cat tmp1 >> $@;
	rm tmp*


