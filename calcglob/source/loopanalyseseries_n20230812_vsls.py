import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

typevar='glob'
typevarlist=['glob','28S28N','60N90N']
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# BROMOFORM SIMULATIONS (bromo08 and additional-output simulations)
#-----------------------
expidlist=[ \
            'NHISTfrc2_f19_tn14_bromo_08'         , 'NSSP585frc2_f19_tn14_bromo_08', \
            'NHISTfrc2_f19_tn14_bromo_08_r1850ext', 'NSSP585frc2_f19_tn14_bromo_08_r2015ext', \
            'NHISTfrc2_f19_tn14_bromo_08_r1850ext', 'NSSP585frc2_f19_tn14_bromo_08_r2015ext', \
            'NHISTfrc2_f19_tn14_bromo_08_r1850ext', 'NSSP585frc2_f19_tn14_bromo_08_r2015ext', \
            'NHISTfrc2_f19_tn14_bromo_08_r1850ext', 'NSSP585frc2_f19_tn14_bromo_08_r2015ext']

refidlist=expidlist

wlist=[1.,0.]

#
legendlist=['emission', '', \
            'chemical sink', '', \
            'photolysis', '', \
            'CHBR'+r'$_3$'+'+OH', '', \
            'photolysis plus '+'CHBR'+r'$_3$'+'+OH',''] 
#
smoothlist=[0,0,0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0,0,0,0]
#
colorlist=[0,0,1,1,2,2,3,3,4,4]
#
variablelist=['SFCHBR3','SFCHBR3', \
              'minusGS_CHBR3','minusGS_CHBR3', \
              'r_jchbr3_columnburden','r_jchbr3_columnburden', \
              'r_CHBR3_OH_columnburden','r_CHBR3_OH_columnburden', \
              'r_jchbr3_CHBR3_OH_columnburden','r_jchbr3_CHBR3_OH_columnburden']
#
code='n20230812_vsls_rerun_chem'
#
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.5')
#
descriptionlocal=''
for typevar in typevarlist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=descriptionlocal,code=code,figlayout=figlayout,colorlist=colorlist)

# BROMOFORM SIMULATIONS (bromo08 and additional-output simulations)
#-----------------------
expidlist=[ \
            'NHISTfrc2_f19_tn14_bromo_08'         , 'NSSP585frc2_f19_tn14_bromo_08', \
            'NHISTfrc2_f19_tn14_bromo_08_r1850ext', 'NSSP585frc2_f19_tn14_bromo_08_r2015ext', \
            'NHISTfrc2_f19_tn14_bromo_08_r1850ext', 'NSSP585frc2_f19_tn14_bromo_08_r2015ext', \
            'NHISTfrc2_f19_tn14_bromo_08_r1850ext', 'NSSP585frc2_f19_tn14_bromo_08_r2015ext', \
            'NHISTfrc2_f19_tn14_bromo_08_r1850ext', 'NSSP585frc2_f19_tn14_bromo_08_r2015ext']

refidlist=expidlist

wlist=[1.,0.]

#
legendlist=['CHBR'+r'$_3$'+' lifetime', '', \
            'CHBR'+r'$_3$'+' lifetime', '', \
            'CHBR'+r'$_3$'+' lifetime (chemical loss)', '', \
            'CHBR'+r'$_3$'+' lifetime (photolysis)', '',  \
            'CHBR'+r'$_3$'+' lifetime (OH reaction)', '']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0,0,0,0,0]
#
colorlist=[0,0,1,1,2,2,3,3,4,4]
#
variablelist=['TAU_CHBR3','TAU_CHBR3', \
              'TAU_CHBR3','TAU_CHBR3', \
              'TAU2_CHBR3', 'TAU2_CHBR3', \
              'TAU_CHBR3_from_jchbr3','TAU_CHBR3_from_jchbr3',\
              'TAU_CHBR3_from_CHBR3_OH','TAU_CHBR3_from_CHBR3_OH']
#
code='n20230812_vsls_rerun_chem'
#
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.5')
#
descriptionlocal=''
for typevar in typevarlist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=descriptionlocal,code=code,figlayout=figlayout,colorlist=colorlist)

# BROMOFORM SIMULATIONS (bromo08 and additional-output simulations)
#-----------------------
expidlist=[ \
            'N1850frc2_f19_tn14_bromo_08', \
            'NHISTfrc2_f19_tn14_bromo_08', \
            'NSSP585frc2_f19_tn14_bromo_08', \
            'NHISTfrc2_f19_tn14_bromo_08_r1850ext', \
            'NSSP585frc2_f19_tn14_bromo_08_r2015ext'] 

refidlist=expidlist

wlist=[1.,0.]

#
legendlist=['piControl-bromo08', \
            'historical-bromo08', \
            'ssp585-bromo08', \
            'historical-bromo08 (extra)', \
            'ssp585-bromo08 (extra)']
#
smoothlist=[0,0,0,0,0]
#            
shiftlist=[-2100+1850,0,0,0,0]
#
colorlist=[0,1,2,3,4]
#
variablelist=['SFCHBR3','cb_CHBR3']
#
code='n20230812_vsls_rerun'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
for typevar in typevarlist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


typevar='glob'

# BROMOFORM SIMULATIONS (bromo08 and full-chemistry)
#-----------------------
expidlist=[ \
            'N1850frc2_f19_tn14_bromo_08', \
            'NHISTfrc2_f19_tn14_bromo_08', \
            'NSSP585frc2_f19_tn14_bromo_08']

refidlist=expidlist

wlist=[1.,0.]

#
legendlist=['piControl-bromo08', \
            'historical-bromo08', \
            'ssp585-bromo08']
#
smoothlist=[0,0,0]
#            
shiftlist=[-2100+1850,0,0]
#
colorlist=[0,1,2]
#
variablelist=['FSDSC','FSNTOAC','O3_columnburden']
#
code='n20230812_vsls'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar='60N90N',freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# BROMOFORM SIMULATIONS (bromo08 and full-chemistry)
#-----------------------
expidlist=[ \
            'N1850frc2_f19_tn14_bromo_08', \
            'NHISTfrc2_f19_tn14_bromo_08', \
            'NSSP585frc2_f19_tn14_bromo_08', \
            'N1850vsls_tropstratchem_prep_f09_nt14_20220223_test14', \
            'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03', \
            'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01']

refidlist=expidlist

wlist=[1.,0.]

#
legendlist=['piControl-bromo08', \
            'historical-bromo08', \
            'ssp585-bromo08', \
            'piControl-fullchem', \
            'historical-fullchem', \
            'ssp585-fullchem']
#
smoothlist=[0,0,0,0,0,0]
#            
shiftlist=[-2100+1850,0,0,1790,0,0]
#
colorlist=[0,1,2,3,4,5]
#
#variablelist=['TAU_CHBR3','TAU2_CHBR3','SFCHBR3','CHBR3_SRF','CHBR3_surfacelayer','cb_CHBR3']
variablelist=['TAU_CHBR3',             'SFCHBR3','CHBR3_SRF','CHBR3_surfacelayer','cb_CHBR3', \
              'SFDMS','TREFHT','tempocn','U10','CLDTOT','CLDLOW','CLDMED','CLDHGH','TAU_DMS','cb_DMS','DMS_SRF','EMI_SALT_TOT_noresm2']   
#
code='n20230812_vsls'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# BROMOFORM SIMULATIONS 
#----------------------
# OH
variablelist=['OH_surfacelayer','OH_surfacelayer','OH_surfacelayer','OH_SRF','OH_SRF','OH_SRF']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
# NO3
variablelist=['NO3_surfacelayer','NO3_surfacelayer','NO3_surfacelayer','NO3_SRF','NO3_SRF','NO3_SRF']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
# HO2
variablelist=['HO2_surfacelayer','HO2_surfacelayer','HO2_surfacelayer','HO2_SRF','HO2_SRF','HO2_SRF']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)
# O3
variablelist=['O3_surfacelayer','O3_surfacelayer','O3_surfacelayer','O3_SRF','O3_SRF','O3_SRF']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,colorlist=colorlist)


# STANDARD CMIP6 SIMULATIONS (to check difference in wind between 1x1 and 2x2)
#-------------------------------------------------------------------------------------------------
expidlist=[ \
            'N1850_f19_tn14_20190621ext', \
            'NHIST_f19_tn14_20190625ext', \
            'NSSP585frc2_f19_tn14_20191014', \
            'N1850frc2_f09_tn14_20191001ext', \
            'NHISTfrc2_f09_tn14_20191001ext', \
            'NSSP585frc2_f09_tn14_20191105']

refidlist=expidlist

wlist=[1.,0.]

#
legendlist=['piControl-2x2', \
            'historical-2x2', \
            'ssp585-2x2', \
            'piControl-1x1', \
            'historical-1x1', \
            'ssp585-1x1']
#
smoothlist=[0,0,0,0,0,0]
#            
shiftlist=[-1600+1850,0,0,-1200+1850,0,0]
#
colorlist=[0,1,2,3,4,5]
#
variablelist=['U10','EMI_SALT_TOT_noresm2','SFDMS','cb_DMS','TAU_DMS','CLDTOT','CLDLOW','CLDMED','CLDHGH']
#
code='n20230812_vsls_cmip6'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
