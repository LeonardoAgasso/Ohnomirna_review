.DELETE_ON_ERROR:

ORG_CAP := Hsa
ORG := hsa


%.gene_pairs.name.tsv:
	ln -s ../../OhnomiRNAs/dataset/gene_pairs/$@ ./$@

mgdb_3_$(ORG).premirna_paralog_pairs.extended_info.tsv:
	ln -s ../3_retrieve_$(ORG_CAP)_paralogs/$@ ./$@

all_$(ORG)_ensembl_paralogmirna_clean.mirgenedb_and_mribase_info.tsv:
	ln -s ../3_retrieve_$(ORG_CAP)_paralogs/$@ ./$@

mgdb_3_$(ORG).premirna.host_gene.compact.strip_mirna_name.dic:
	ln -s ../2_find_WGD_intragenic/$@ ./$@

mgdb_3_$(ORG).premirna_paralog_pairs.extended_info.host_gene.tsv: mgdb_3_$(ORG).premirna_paralog_pairs.extended_info.tsv mgdb_3_$(ORG).premirna.host_gene.compact.strip_mirna_name.dic
	cat $(word 1, $^) | awk -F"\t" 'NR>1' | translate -a -d -j -v -e intergenic $(word 2, $^) 1 | translate -a -d -j -v -e intergenic $(word 2, $^) 9 | sort | uniq > tmp1;
	cat tmp1 | cut -f2,10 --complement | awk -F"\t" '{print $$1"\t"$$4"\t"$$5"\t"$$6"\t"$$7"\t"$$3"\t"$$2"\t"$$8"\t"$$11"\t"$$12"\t"$$13"\t"$$14"\t"$$10"\t"$$9"\t"$$15"\t"$$16}' | sort | uniq > tmp2;
	echo "#MiRGeneDB_name_1\tgene_ID_1\tgene_name_1\tmirbase_premirna_accession_1\ttranscript_name_1\thost_gene_name_1\thost_gene_ID_1\tMiRGeneDB_name_2\tgene_ID_2\tgene_name_2\tmirbase_premirna_accession_2\ttranscript_name_2\thost_gene_name_2\thost_gene_ID_2" >> $@;
	cat tmp2 >> $@;
	rm tmp*

mgdb_3_$(ORG).premirna_paralog_pairs.extended_info.flagged_SSD_host_gene.tsv: mgdb_3_$(ORG).premirna_paralog_pairs.extended_info.host_gene.tsv paralogs.gene_pairs.name.tsv
	cat $(word 1, $^) | awk -F"\t" 'NR>1' | flag_pairs -l SSD --both-orders -e not_related 6 13 $(word 2, $^) 1 2 | sort | uniq > tmp1;
	echo "#MiRGeneDB_name_1\tgene_ID_1\tgene_name_1\tmirbase_premirna_accession_1\ttranscript_name_1\thost_gene_name_1\thost_gene_ID_1\tMiRGeneDB_name_2\tgene_ID_2\tgene_name_2\tmirbase_premirna_accession_2\ttranscript_name_2\thost_gene_name_2\thost_gene_ID_2\thost_genes_homology" >> $@;
	cat tmp1 >> $@;
	rm tmp*

mgdb_3_$(ORG).premirna_paralog_pairs.extended_info.flagged_WGD_host_gene.tsv: mgdb_3_$(ORG).premirna_paralog_pairs.extended_info.host_gene.tsv ohnologs.gene_pairs.name.tsv
	cat $(word 1, $^) | awk -F"\t" 'NR>1' | flag_pairs -l WGD --both-orders -e not_related 6 13 $(word 2, $^) 1 2 | sort | uniq > tmp1;
	echo "#MiRGeneDB_name_1\tgene_ID_1\tgene_name_1\tmirbase_premirna_accession_1\ttranscript_name_1\thost_gene_name_1\thost_gene_ID_1\tMiRGeneDB_name_2\tgene_ID_2\tgene_name_2\tmirbase_premirna_accession_2\ttranscript_name_2\thost_gene_name_2\thost_gene_ID_2\thost_genes_homology" >> $@;
	cat tmp1 >> $@;
	rm tmp*


all_$(ORG)_ensembl_paralogmirna_clean.mirgenedb_and_mribase_info.host_gene.tsv: all_$(ORG)_ensembl_paralogmirna_clean.mirgenedb_and_mribase_info.tsv mgdb_3_$(ORG).premirna.host_gene.compact.strip_mirna_name.dic
	cat $(word 1, $^) | translate -a -d -j -v -e intergenic $(word 2, $^) 2 | translate -a -d -j -v -e intergenic $(word 2, $^) 10 | sort | uniq > $@

all_$(ORG)_ensembl_paralogmirna_clean.mirgenedb_and_mribase_info.flagged_SSD_host_gene.tsv: all_$(ORG)_ensembl_paralogmirna_clean.mirgenedb_and_mribase_info.host_gene.tsv paralogs.gene_pairs.name.tsv
	cat $(word 1, $^) | awk -F"\t" 'NR>1' | flag_pairs -l SSD --both-orders -e not_SSD 5 13 $(word 2, $^) 1 2 | sort | uniq > $@

all_$(ORG)_ensembl_paralogmirna_clean.mirgenedb_and_mribase_info.flagged_WGD_host_gene.tsv: all_$(ORG)_ensembl_paralogmirna_clean.mirgenedb_and_mribase_info.host_gene.tsv ohnologs.gene_pairs.name.tsv
	cat $(word 1, $^) | awk -F"\t" 'NR>1' | flag_pairs -l WGD --both-orders -e not_WGD 5 13 $(word 2, $^) 1 2 | sort | uniq > $@
