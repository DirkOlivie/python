import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# 1. N1850
#-----------------------
expidlist=[ \
           'N1850_f19_tn14_20190621ext', \
           'N1850_f19_tn14_20241127_test01', \
           'N1850_tropstratchem_f19_tn14_20241127_test01']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'noresm2 (CMIP6)', \
            'noresm2.3', \
            'noresm2.3 (chemistry)']
#
smoothlist=[5,5,5]
#
colorlist=[0,1,2]
linestylelist=[0,0,0]
#            
shiftlist=[0,0,0]
#
variablelist=['PRECT', \
              'cb_SOA_A1NA', \
              'TGCLDLWP','TGCLDIWP', 'TREFHT', \
              'U10', \
              'CDNUMC','NUMICE_columnburden','NUMLIQ_columnburden','N_AER_columnburden', \
              'SFisoprene','SFmonoterp', \
              'SFDMS','TREFHT','SWCF','LWCF','FSLNT', \
              'CLDTOT','CLDLOW','CLDMED','CLDHGH', \
              'cb_SULFATE','cb_OM','cb_SALT','cb_DUST','cb_BC', \
              'ICEFRAC']
#
code='n20250315_noresm2.3_cpl_fullchem'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
#typevarlist=['glob','NHLAND','SHSEA','SH','NH','SHLAND','NHSEA']
typevarlist=['glob','NH','SH']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# ocean temperature
variablelist=['tempocn']
typevarlist=['glob']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# ocean amoc
variablelist=['mmflxdmax26.0Nocn']
typevarlist=['glob','atlarc']
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# ocean temperature
variablelist=['ICEFRAC']
typevarlist=['NH','SH']
freqtypelist=['SEP','MAR']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)





