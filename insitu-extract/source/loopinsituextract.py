import loopinsituextract2


locationlist=['AmsterdamIsland']
expidlist=['n1850.ne16pg3_tn14.noresm3_0_beta06.Best_c8_4p7.2025-12-01']
variablelist=['TREFHT','PS','SULFATE_SRF','DMS_SRF']

loopinsituextract2.loopinsituextract2(expidlist=expidlist, variablelist=variablelist, locationlist=locationlist)
