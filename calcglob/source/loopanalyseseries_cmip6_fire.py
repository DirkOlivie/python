import numpy as np

import loopanalyseseries2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

typevar='glob'
#freqtype='annavg'
freqtype='YEA'
description='varcommon'




# 1pctCO2 + 1pctCO2-rad + 1pctCO2-gcd
#-------------------------------------------------------------------
expidlist=[ \
            'N1PCT_f19_tn14_20190626ext', \
            'N1PCTBGC_f19_tn14_20190629', \
            'N1PCTRADfrc2_f19_tn14_20191213'] 

refidlist=expidlist
wlist=[1.,0.]

#
legendlist=['1pctCO2', \
            '1pctCO2-bgc', \
            '1pctCO2-rad']
#
colorlist=[0,1,2]
#
nexpid=len(expidlist)
smoothlist=np.zeros(nexpid,dtype=int)+5
shiftlist=[0,0,0]

#            
variablelist=['FCH4xLANDFRAC']
#
figlayout=cfiglayout.CFigLayout()
#
code='cmip6_fire_1pctco2'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# piControl + historical + ssp585
#-------------------------------------------------------------------
expidlist=[ \
           'NHIST_f19_tn14_20190625ext', \
           'NHIST_02_f19_tn14_20190801ext', \
           'NHIST_03_f19_tn14_20190801ext', \
            \
           'NHISTfrc2_f09_tn14_20191001ext', \
           'NHISTfrc2_02_f09_tn14_20200427ext', \
           'NHISTfrc2_03_f09_tn14_20200519ext', \
            \
           'NSSP585frc2_f19_tn14_20191014', \
            \
           'NSSP585frc2_f09_tn14_20200919', \
            \
           'N1850_f19_tn14_20190621ext', \
            \
           'N1850frc2_f09_tn14_20191001ext']

refidlist=expidlist
wlist=[1.,0.]

#
legendlist=['historical (2x2)','','', \
            'historical (1x1)','','', \
            'ssp5-8.5 (2x2)', \
            'ssp5-8.5 (1x1)', \
            'piControl (2x2)', \
            'piControl (1x1)']
#
colorlist=[0,0,0,1,1,1,2,3,4,5]
#
nexpid=len(expidlist)
smoothlist=np.zeros(nexpid,dtype=int)+5
shiftlist=[0,0,0, \
           0,0,0, \
           0, \
           0, \
           1850-1600, \
           1850-1200]

#            
variablelist=['COL_FIRE_CLOSSxLANDFRAC',\
              'PFT_FIRE_CLOSSxLANDFRAC', \
              'SOMC_FIRExLANDFRAC']
#
figlayout=cfiglayout.CFigLayout()
#
code='cmip6_fire'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# fhist
#-------------------------------------------------------------------
expidlist=['NHIST_f19_tn14_20190625ext', \
           'NHIST_02_f19_tn14_20190801ext', \
           'NHIST_03_f19_tn14_20190801ext', \
           'NFHISTnorpibc_f19_20190810',               \
           'NFHISTnorpibc_02_f19_20190909',             \
           'NFHISTnorpibc_03_f19_20190923',             \
           'NFHISTnorpibc_aeroxidonly_f19_20190810',    \
           'NFHISTnorpibc_aeroxidonly_02_f19_20190909', \
           'NFHISTnorpibc_aeroxidonly_03_f19_20190923', \
           'NFHISTnorpibc_ghgonly_f19_20190810',        \
           'NFHISTnorpibc_ghgonly_02_f19_20190909',     \
           'NFHISTnorpibc_ghgonly_03_f19_20190923',     \
           'NFHISTnorpibc_natonly_f19_20190810',        \
           'NFHISTnorpibc_natonly_02_f19_20190909',     \
           'NFHISTnorpibc_natonly_03_f19_20190923',     \
           'NFHISTnorpibc_ozoneonly_f19_20190924',      \
           'NFHISTnorpibc_ozoneonly_02_f19_20190925',   \
           'NFHISTnorpibc_ozoneonly_03_f19_20190925',   \
           'NFHISTnorpibc_luonly_f19_20191208',         \
           'NFHISTnorpibc_luonly_f19_20191129',         \
           'NFHISTnorpibc_luonly_02_f19_20191129',      \
           'NFHISTnorpibc_luonly_03_f19_20191129']
refidlist=expidlist
wlist=[1.,0.]

#
legendlist=['historical','','', \
            'all','','', \
            'aer+oxid','','', \
            'ghg','','', \
            'nat','','', \
            'ozone','','', \
            'lu','','','']
#
colorlist=[0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,6]
#
nexpid=len(expidlist)
smoothlist=np.zeros(nexpid,dtype=int)+5
shiftlist=np.zeros(nexpid,dtype=int)

#            
variablelist=['FCH4xLANDFRAC']
#
figlayout=cfiglayout.CFigLayout()
#
code='cmip6_fire_fsst'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
