#!/usr/bin/env python3

#############################################################################
# 	Program to extract the most ancient node in a gene tree					#
# 	given a list of gene ids (ENSG...)										#
# 	Actually nothing more than a small modification of the Ensembl API:		#
#############################################################################

import requests, sys

for ENSG in sys.stdin:
	flag = 0
	ENSG = ENSG.rstrip() #Remove the trailing newline
	server = "https://rest.ensembl.org"
	ext = "/genetree/member/id/"+ENSG+"/?"

	r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

	if not r.ok:
		print(ENSG + "\t" + "not_present")
		flag=1

	if flag==0:
		x = r.json()
		firstnode = x["tree"]["taxonomy"]["scientific_name"]
		print(ENSG + "\t" + firstnode)

sys.exit()
