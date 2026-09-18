import analyseseries

def loopanalyseseries2(expidlist,legendlist,variablelist,typevar,freqtype,code) :

    for variable in variablelist :
        analyseseries.analyseseries(expidlist=expidlist,legendlist=legendlist,variable=variable,typevar=typevar,freqtype=freqtype,code=code)
  

# MAIN PROGRAM

expidlist=['FHIST_f19_f19_mg17_20211015', \
           'FHIST_SO2ANTEUR_f19_f19_mg17_20211015', \
           'FHIST_SO2ANTNAM_f19_f19_mg17_20211015', \
           'NFHISTnorbc_f19_20210611', \
           'NFHISTnorbc_SO2ANTEUR_f19_20210611', \
           'NFHISTnorbc_SO2ANTNAM_f19_20210611']
legendlist=['CESM2.1.3', \
            'CESM2.1.3 (Europe)', \
            'CESM2.1.3 (North-Am.)', \
            'NorESM2', \
            'NorESM2 (Europe)', \
            'NorESM2 (North-Am.)']
#
variablelist=['TREFHT','QREFHT','PBLH','PS','SWCF','LWCF','ICEFRAC','FSNT','FLNT', \
              'CLDLOW','CLDMED','CLDHGH','CLDTOT','CLDLIQ','CLDICE', \
              'CDNUMC', \
              'DMS_SRF','SO2_SRF', \
              'SFSO2','SO2_CMXF', \
              'LHFLX','SHFLX', \
              'TGCLDCWP','TGCLDIWP','TGCLDLWP']
#
variablelist=['FSLNT','EMI_SO2_TOT_noresm2']
#
typevar='glob'
#typevar='SEA'
freqtype='annavg'
code='cesm2.1.3'
#
loopanalyseseries2(expidlist=expidlist,legendlist=legendlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,code=code)
