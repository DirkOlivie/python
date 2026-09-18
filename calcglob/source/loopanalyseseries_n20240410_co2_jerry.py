import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='typevarcommon'
# 
# 1. NorESM2-LM and NorESM2-LM-C : absolute
#------------------------------------------
expidlist=['N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027', \
           'N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027', \
           'N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027', \
           'N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027']
#
#expidlist=['N1850_f19_tn14_20190730esm', \
#           'N1850_f19_tn14_20190730esm', \
#           'N1850_f19_tn14_20190730esm', \
#           'N1850_f19_tn14_20190730esm', \
#           'N1850_f19_tn14_20190730esm', \
#           'N1850_f19_tn14_20190730esm', \
#           'N1850_f19_tn14_20190730esm', \
#           'N1850_f19_tn14_20190730esm']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
variablelist=['TMCO2','TMCO2_FFF','TMCO2_LND','TMCO2_OCN'] #, \
#variablelist=['CO2_columnburden','CO2_FFF_columnburden','CO2_LND_columnburden','CO2_OCN_columnburden']
legendlist=variablelist
#
#smoothlist=[0,0,0,0]
smoothlist=[5,5,5,5]#,5,5,5,5]
#
colorlist=[0,1,2,3]#,4,5,6,7]
#            
shiftlist=[0,0,0,0]#,0,0,0,0]
#
code='n20240410_co2_jerry'
#
#figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

variablelist=['SFCO2','SFCO2_FFF','SFCO2_LND','SFCO2_OCN']
legendlist=variablelist
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)





