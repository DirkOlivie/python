import analyseseries

def loopanalyseseries2(expidlist,legendlist,variablelist,typevar,freqtype,code) :

    for variable in variablelist :
        analyseseries.analyseseries(expidlist=expidlist,legendlist=legendlist,variable=variable,typevar=typevar,freqtype=freqtype,code=code)
  

# MAIN PROGRAM
expidlist=['NF1850norbc_f19_f19_20210530', \
#           'NF1850norbc_f19_f19_20210923', \
           'NF1850norbc_f19_f19_20211013', \
           'NF1850norbc_f19_20211113_test17', \
           'F2000climo_f09_ver2.1.3_20211005', \
           'F2000climo_f09_ver2.2_20211005', \
           'F2000climo_f09_20211109_cesm2.2_test04']
#           'NF1850norbc_f19_20211101_noresm2_test01', \
#           'NF1850norbc_f19_20211101_noresm2.2_test01']
legendlist=['NorESM2', \
#            'NorESM2.2 (flux=0)', \
            'NorESM2.2', \
            'NorESM2.2 (Clubb 2.1.3)', \
            'CESM2.1.3', \
            'CESM2.2', \
            'CESM2.2 (Clubb 2.1.3)']
#            'NorESM2 (flux=1, gamma=0.308)', \
#            'NorESM2.2 (flux=1, gamma=0.308)']  
#
variablelist=['TREFHT','QREFHT','PBLH','PS','SWCF','LWCF','ICEFRAC','FSNT','FLNT', \
              'CLDLOW','CLDMED','CLDHGH','CLDTOT','CLDLIQ','CLDICE', \
              'CDNUMC', \
              'DMS_SRF','SO2_SRF', \
              'SFSO2','SO2_CMXF', \
              'LHFLX','SHFLX', \
              'TGCLDCWP','TGCLDIWP','TGCLDLWP', \
              'FSLNT', \
              'PRECC','PRECL', \
              'ELAI','LAISHA','LAISUN','TLAI', \
              'SOILWATER_10CM', \
              'TOTSOILLIQ']
#
variablelist=['FSNO']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='testnoresm2.2'
#
loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,code=code)
#
variablelist=['TREFHT']
typevar='LAND'
code='testnoresm2.2_land'
#
loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,code=code)
