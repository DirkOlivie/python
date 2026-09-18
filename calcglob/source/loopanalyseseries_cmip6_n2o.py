import numpy as np

import loopanalyseseries2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

typevarlist=['glob']
#freqtype='annavg'
freqtype='YEA'
description='varcommon-typevarcommon'




# 1pctCO2 + 1pctCO2-rad + 1pctCO2-gcd
#-------------------------------------------------------------------
expidlist=[ \
            'N1850_f19_tn14_20190621', \
            'N1PCT_f19_tn14_20190626ext', \
            'N1PCTBGC_f19_tn14_20190629', \
            'N1PCTRADfrc2_f19_tn14_20191213']
#            'NCO2x4_f19_tn14_20190624']

refidlist=expidlist
wlist=[1.,0.]

#
legendlist=['piControl', \
            '1pctCO2', \
            '1pctCO2-bgc', \
            '1pctCO2-rad']
#            'abrupt-4xCO2']
#
colorlist=[0,1,2,3]
#
nexpid=len(expidlist)
smoothlist=np.zeros(nexpid,dtype=int)+5
shiftlist=[-1600+1,0,0,0]

#            
variablelist=['F_N2O_DENIT_NITxLANDFRAC', \
              'F_N2O_DENIT_NITxLANDFRAC_as_N2O', \
              'NDEP_TO_SMINNxLANDFRAC']
#
figlayout=cfiglayout.CFigLayout()
#
code='cmip6_n2o_1pctco2'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# piControl + historical + ssp585
#-------------------------------------------------------------------
expidlist=[ \
           'NHIST_f19_tn14_20190625ext', \
           'NHIST_02_f19_tn14_20190801ext', \
           'NHIST_03_f19_tn14_20190801ext', \
            \
           'NHISTfrc2_f09_tn14_20191001ext', \
#           'NHISTfrc2_02_f09_tn14_20200427ext', \
#           'NHISTfrc2_03_f09_tn14_20200519ext', \
            \
           'NSSP245frc2_f19_tn14_20191014', \
           'NSSP245frc2_f09_tn14_20191105', \
            \
           'NSSP370frc2_f19_tn14_20191014', \
           'NSSP370frc2_f09_tn14_20191105', \
            \
#           'NSSP126frc2_f19_tn14_20191014', \
#           'NSSP245frc2_f19_tn14_20191014', \
#           'NSSP370frc2_f19_tn14_20191014', \
#           'NSSP585frc2_f19_tn14_20191014', \
            \
#           'NSSP126frc2_f09_tn14_20191105', \
#           'NSSP245frc2_f09_tn14_20191105', \
#           'NSSP370frc2_f09_tn14_20191105', \
#           'NSSP585frc2_f09_tn14_20191105', \
            \
           'N1850_f19_tn14_20190621ext', \
            \
           'N1850frc2_f09_tn14_20191001ext']

refidlist=expidlist
wlist=[1.,0.]

#
legendlist=['historical (2x2)','','', \
            'historical (1x1)', \
            'ssp2-4.5 (2x2)', \
            'ssp2-4.5 (1x1)', \
            'ssp3-7.0 (2x2)', \
            'ssp3-7.0 (1x1)', \
            'piControl (2x2)', \
            'piControl (1x1)']
#
colorlist=[0,0,0,1,2,3,4,5,6,7]#,8,9,10,11]
#
nexpid=len(expidlist)
smoothlist=np.zeros(nexpid,dtype=int)+5
shiftlist=[0,0,0, \
           0, \
           0,0, \
           0,0, \
           1850-1600, \
           1850-1200]

#
variablelist=['F_N2O_DENIT_NITxLANDFRAC', \
              'F_N2O_DENIT_NITxLANDFRAC_as_N2O', \
              'NDEP_TO_SMINNxLANDFRAC', \
              'NFERTILIZATIONxLANDFRAC']            
#
figlayout=cfiglayout.CFigLayout()
#
code='cmip6_n2o'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


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
variablelist=['F_N2O_DENIT_NITxLANDFRAC', \
              'NDEP_TO_SMINNxLANDFRAC']
#
figlayout=cfiglayout.CFigLayout()
#
code='cmip6_n2o_fsst'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
