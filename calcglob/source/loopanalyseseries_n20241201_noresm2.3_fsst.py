import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# noresm2.3

# 1. N1850
#-----------------------
expidlist=['NF1850norbc_aer2014_f19_20191025', \
           'NF1850norbc_aer2014_f19_f19_20231204_test17', \
           'NF1850norbc_aer2014_f19_f19_20241127_test01', \
           'NF1850norbc_aer2014_f19_f19_20241127_test05', \
           'NF1850norbc_aer2014_f19_f19_20241127_test06', \
# 
           'NF1850norbc_f19_20191025len30'        , \
           'NF1850norbc_f19_f19_20231204_test17'        , \
           'NF1850norbc_f19_f19_20241127_test01'        , \
           'NF1850norbc_f19_f19_20241127_test05'        , \
           'NF1850norbc_f19_f19_20241127_test06'        ]
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'noresm2 (CMIP6)', \
            'noresm2.1', \
            'noresm2.3', \
            'noresm2.3 (old soa-yield)', \
            'noresm2.3 (secondary ice)', \
            '', \
            '', \
            '', \
            '', \
            '']
#            'noresm2.1 + SH/TS']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,0,1,2,3,4]
linestylelist=[0,0,0,0,0,1,1,1,1,1]
#            
shiftlist=[0,0,0,0,0,0,0,0,0,0]
#
variablelist=[ \
              'PRECT', \
#             'cb_SOA_A1NA', \
#              'TGCLDLWP','TGCLDIWP', 'TREFHT', \
              'U10', \
              'CDNUMC','NUMICE_columnburden','NUMLIQ_columnburden','N_AER_columnburden', \
              'SFisoprene','SFmonoterp', \
              'SFDMS','TREFHT','SWCF','LWCF','FSLNT', \
              'CLDTOT','CLDLOW','CLDMED','CLDHGH', \
              'cb_SULFATE','cb_OM','cb_SALT','cb_DUST','cb_BC', \
              'ICEFRAC']
#
variablelist=['FSLNT','SWCF','LWCF']
#
code='n20241201_noresm2.3_fsst'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
