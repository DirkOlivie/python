import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


freqtype='YEA'
typevar='glob'
description='varcommon-typevarcommon'
generalcode='n20240822_camsvsls'


# ALL EXPERIMENTS (NEW + BROMO-08 + FULLCHEM + CMIP6)
#------------------------------------------------------------------------
#
expidlist=[ \
           'NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim01', \
           'NHISTfrc2sdyn_02_f09_tn14_bromo_r1995_sim01', \
           'NHISTSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03', \
           'NHISTfrc2_f19_tn14_bromo_08', \
           'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
           \
           'NHIST_f19_tn14_20190710', \
           'NHIST_02_f19_tn14_20190813', \
           'NHIST_03_f19_tn14_20190813', \
           \
           'NHISTfrc2_f09_tn14_20191025', \
           'NHISTfrc2_02_f09_tn14_20200519', \
           'NHISTfrc2_03_f09_tn14_20200619'] 
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['nudged', \
            'nudged [memb 2]', \
            'nudged [energy]', \
#            '', \
            'bromo08 [2x2]', \
            'fullchem', \
            \
            'CMIP6 [2x2]', \
            '', \
            '', \
            \
            'CMIP6', \
            '', \
            ''] 
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5,5,5,6,6,6]
#

# variables
variablelist=['U10','PBLH','TREFHT','QREFHT','FSLNT', \
              'SFDMS','DMS_SRF','cb_DMS', \
              'PRECT', \
              'CLDTOT','CLDLOW','CLDMED','CLDHGH','CLDICE','CLDLIQ', \
              'EMI_DUST_TOT_noresm2']
#
typevarlist=['glob','LAND','SEA']

code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# BROMOFORM-CONTAINING EXPERIMENTS
#------------------------------------------------------------------------
#
expidlist=[ \
           'NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim01', \
           'NHISTfrc2sdyn_02_f09_tn14_bromo_r1995_sim01', \
           'NHISTSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03', \
           'NHISTfrc2_f19_tn14_bromo_08', \
           'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['nudged', \
            'nudged [memb 2]', \
            'nudged [energy]', \
            'bromo08 [2x2]', \
            'fullchem']
#
smoothlist=[0,0,0,0,0]
#
shiftlist=[0,0,0,0,0]
#
colorlist=[0,1,2,3,4]
#

# variables
variablelist=['SFCHBR3','CHBR3_SRF','cb_CHBR3']
#
typevarlist=['glob','LAND','SEA']

code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
# ALL EXPERIMENTS (NEW + BROMO-08 + FULLCHEM + CMIP6)
#------------------------------------------------------------------------
#
expidlist=[ \
           'NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim01', \
           'NHISTfrc2sdyn_02_f09_tn14_bromo_r1995_sim01', \
           'NHISTSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['nudged', \
            'nudged [memb 2]', \
            'nudged [energy]']
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,0]
#
colorlist=[0,1,2]
#

# variables
variablelist=['U10','PBLH','TREFHT','QREFHT','FSLNT', \
              'SFDMS','DMS_SRF','cb_DMS', \
              'PRECT', \
              'CLDTOT','CLDLOW','CLDMED','CLDHGH','CLDICE','CLDLIQ', \
              'EMI_DUST_TOT_noresm2', \
              'SFCHBR3','CHBR3_SRF','cb_CHBR3']
#
typevarlist=['glob','LAND','SEA']

code=generalcode+'_camsonly'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


