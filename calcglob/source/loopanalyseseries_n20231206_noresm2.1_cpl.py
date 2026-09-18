import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon'


# stratospheric aerosol

# 1. N1850
#-----------------------
expidlist=[ \
           'N1850_f19_tn14_20190621ext', \
           'N1850_f19_tn14_20231204_test05', \
           'N1850_f19_tn14_20231204_test03', \
           'N1850_f19_tn14_20231204_test04', \
           'N1850_f19_tn14_20231204_test06', \
           'N1850_f19_tn14_20231204_test07', \
           'N1850_f19_tn14_20231204_test02']
#           'N1850_f19_tn14_20231204_test10']
#           'N1850_f19_tn14_20231204_test09']

#           'N1850_f19_tn14_20231204_test08']
#          'N1850frc2_f09_tn14_20191001ext']
#           'N1PCT_f19_tn14_20190626']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[ \
            'noresm2 (CMIP6)', \
            'noresm2.1 (no CAM corr.)', \
            'noresm2.1 (no ice-delimiter corr.)', \
            'noresm2.1 (no het. freez. corr.)', \
            'noresm2.1 (no koagsub corr.)', \
            'noresm2.1 (no dry dep. corr.)', \
            'noresm2.1']
#            'noresm2.1 + Hofer']
#            'noresm2 (CMIP6, 1x1)']
#            'noresm2 1pct-CO2' ]
#
#smoothlist=[0]#,0,0,0]
smoothlist=[5,5,5,5,5,5,5]
#smoothlist=[10,10,10,10,10,10,10,10]
#
colorlist=[0,1,2,3,4,5,6]
#            
shiftlist=[0,0,0,0,0,0,0]#-1200+1600]#,-1+1600]
#
variablelist=['TGCLDLWP','TGCLDIWP', \
              'U10', \
              'CDNUMC','NUMICE_columnburden','NUMLIQ_columnburden','N_AER_columnburden', \
              'SFisoprene','SFmonoterp', \
              'SFDMS','TREFHT','SWCF','LWCF','FSLNT', \
              'CLDTOT','CLDLOW','CLDMED','CLDHGH', \
              'cb_SULFATE','cb_OM','cb_SALT','cb_DUST','cb_BC', \
              'ICEFRAC']
#
code='n20231206_noresm2.1_cpl'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob','NHLAND','SHSEA','SH','NH','SHLAND','NHSEA']
freqtypelist=['YEA']
#
# atmosphere
for freqtype in freqtypelist : 
    for typevar in typevarlist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# ocean temperature
variablelist=['tempocn']
typevarlist=['glob']
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# ocean amoc
variablelist=['mmflxdmax26.0Nocn']
typevarlist=['glob','atlarc']
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# 2. N1850 : INCLUDING ADDITIONAL BETZY TESTS
#--------------------------------------------
expidlist=['N1850_f19_tn14_20190621ext', \
           'N1850_f19_tn14_20231204_test02', \
           'N1850_f19_tn14_20231204_test03', \
           'N1850_f19_tn14_20231204_test04', \
           'N1850_f19_tn14_20231204_test05', \
           'N1850_f19_tn14_20231204_test06', \
           'N1850_f19_tn14_20231204_test07', \
           'N1850frc2_f09_tn14_20191001ext', \
           'N1850_f19_tn14_20210317b', \
           'N1850_f19_tn14_20210409b', \
           'N1850_f19_tn14_20210409c']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['noresm2 (CMIP6)', \
            'noresm2.1', \
            'noresm2.1 (no ice-delimiter corr.)', \
            'noresm2.1 (no het. freez. corr.)', \
            'noresm2.1 (no CAM corr.)', \
            'noresm2 (CMIP6, 1x1)', \
            'noresm2 (CMIP6, betzy)',
            'noresm2 (CMIP6, betzy)',
            'noresm2 (CMIP6, betzy)']         
#
#smoothlist=[0,0,0,0,0,0,0,0,0]
smoothlist=[5,5,5,5,5,5,5,5,5]
#smoothlist=[10,10,10,10,10,10,10]
#
colorlist=[0,1,2,3,4,5,6,7,8]
#            
shiftlist=[0,0,0,0,0,-1200+1600,0,0,0]
#
variablelist=['tempocn']
#
code='n20231206_noresm2.1_cpl'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
#for freqtype in freqtypelist : 
#    for typevar in typevarlist : 
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
