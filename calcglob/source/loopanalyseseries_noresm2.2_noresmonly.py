import analyseseries

def loopanalyseseries2(expidlist,legendlist,variablelist,typevar,freqtype,code) :

    for variable in variablelist :
        analyseseries.analyseseries(expidlist=expidlist,legendlist=legendlist,variable=variable,typevar=typevar,freqtype=freqtype,code=code)
  

# MAIN PROGRAM
expidlist=['NF1850norbc_f19_f19_20210530', \
#           'NF1850norbc_f19_f19_20210923', \
           'NF1850norbc_f19_f19_20211013', \
           'NF1850norbc_f19_20211113_test17']
#           'NF1850norbc_f19_20211101_noresm2_test01', \
#           'NF1850norbc_f19_20211101_noresm2.2_test01']
legendlist=['NorESM2', \
#            'NorESM2.2 (flux=0)', \
            'NorESM2.2', \
            'NorESM2.2 (Clubb 2.1.3)']
#            'NorESM2 (flux=1, gamma=0.308)', \
#            'NorESM2.2 (flux=1, gamma=0.308)']  
#
variablelist=['GPP','NPP', \
              'SFisoprene','SFmonoterp', \
              'MEG_isoprene','MEG_monoterp','MEG_carene_3','MEG_ocimene_t_b','MEG_myrcene','MEG_limonene','MEG_pinene_b','MEG_pinene_a','MEG_sabinene', \
              'SFDST_A2','SFDST_A3']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='testnoresm2.2_only'
#
loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,code=code)
