import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'
#figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
figlayout=cfiglayout.CFigLayout()
code='n20251107_n2olandocean_spinup'

# OCN #
#-----#
expidlist=['N1850_f19_tn14_20190621ext', \
           'Ncyc-spinup-01-1deg-noresm2.1.3BLOM-enhanced-v1.6.9-NOINYOC', \
           'NorESM-Ncyc_N1850_f19_tn14_NorESM2.0.9_BLOMv1.6.X_20251128T2117']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2-LM (piControl)', \
            'spinup (2025)', \
            'spinup (2026)']
#
smoothlist=[0,0,0]
#
colorlist=[0,1,2]
#            
shiftlist=[-1599,0,0]
#
variablelist=[\
              'tempocn','sssgaocn','sstgaocn','salngaocn']
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# AMOC #
#------#
typevarlist=['glob','atlarc']
variablelist=['mmflxdmax26.0Nocn']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# ATM/LND #
#---------#

expidlist=['N1850_f19_tn14_20190621ext', \
           'NorESM-Ncyc_N1850_f19_tn14_NorESM2.0.9_BLOMv1.6.X_20251128T2117']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['NorESM2-LM (piControl)', \
            'spinup (2026)']
#
smoothlist=[0,0]
#
colorlist=[0,2]
#            
shiftlist=[-1599,0]
#
variablelist=[\
              'TREFHT', 'PRECT', \
              'SWCF','LWCF', 
              'U10', \
              'cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT', \
              'AOD_VISdivDAYFOC', \
              'SFDMS']
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)



