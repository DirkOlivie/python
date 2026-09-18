import numpy as np
import loopanalysescatter2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist
import expidlist2attributelist

# MAIN PROGRAM
# CORRECTION
#   2024-11-24 : replaced NorESM2-LM_pdClim-controlfixO3-2050ssp370_r1i1p1f1_gn by NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn



generalcode='n20260426_noresm2.5_picontrol'

figlayout=cfiglayout.CFigLayout('')

# 1.a ne16pg3 - n1850
#----------------------------------
# x-axis
description='varcommon-typevarcommon'
expXlist=[\
          'n1850.ne16pg3_tn14.noresm3_0_beta09.2025-12-19', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.LandSpinup.2025-12-24', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.Run3.2025-12-30', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.Run4.2026-01-06', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.2026-01-08', \
          'n1850.ne16pg3_tn14.noresm3_0_beta10.Run6.2026-01-23', \
          'n1850.ne16pg3_tn14.noresm3_0_beta10.Run7.2026-01-26', \
          'n1850.ne16pg3_tn14.noresm3_0_beta11.Run8.2026-02-07', \
          'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11', \
          'n1850.ne16pg3_tn14.noresm3_0_beta12a.Run10_hyb.2026-03-28', \
#          'n1850.ne16pg3_tn14.noresm3_0_beta13a.Run11_drydep_oldBLOM.2026-04-17'
          'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14.Olivia.2026-05-28', \
          'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-A.Olivia.2026-06-01', \
          'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-A2.Olivia.2026-06-03', \
          'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-B.Olivia.2026-06-03', \
          'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-C.Olivia.2026-06-04', \
          'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-D.Olivia.2026-06-04', \
          'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-F.Olivia.2026-06-05', \
          'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-G.Olivia.2026-06-06', \
          'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-H.Olivia.2026-06-08', \
          'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-I.Olivia.2026-06-08', \
          'n1850.ne16pg3_tn14.noresm3_0_beta18.Run14-F_blom_cv_1p2.2026-06-12', \
          'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15.Olivia.2026-06-08', \
          'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-B.Olivia.2026-06-11', \
          'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-C.Olivia.2026-06-15', \
          'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-D.Olivia.2026-06-17', \
          'n1850.ne16pg3_tn14.noresm3_0_beta19.Run15-E.Olivia.2026-06-18', \
          'n1850.ne16pg3_tn14.noresm3_0_beta20.Run15-F.Olivia.2026-06-22', \
          'n1850.ne16pg3_tn14.noresm3_0_beta20.Run16.Olivia.2026-07-02', \
          'n1850.ne16pg3_tn14.noresm3_0_beta20.470.ref461.20260626', \
          'n1850.ne16pg3_tn14.noresm3_0_beta20.473.ref461.20260630', \
          'n1850.ne16pg3_tn14.noresm3_0_beta20.474.ref461.20260630', \
          'n1pctCO2.ne16pg3_tn14.beta20.2026-06-12', \
          'n1pctCO2-RAD.ne16pg3_tn14.beta20.2026-06-24', \
          'n1850.ne16pg3_tn14.noresm3_0_beta21.cmeps-latent-heat-bugfix.2026-07-23']  
#
refXlist=expXlist
# 
nexpid=len(expXlist)
#
expXyear0list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year0')
expXyear1list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year1')
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA']*nexpid
wXlist=[1.,0.]
# y-axis
expYlist=expXlist
refYlist=refXlist
expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=wXlist

# variables
varXlist=['FSLNT'        ,'FSLNT'          ,'hflxocn'      ]
varYlist=['tempocn_trend','tempgaocn_trend','tempocn_trend']
nvar=len(varXlist)
typevarXlist=['glob']*nvar
typevarYlist=['glob']*nvar
# 
legendlist=[ \
            '2025-12-19', \
            '2025-12-24', \
            'Run3','Run4','Run5','Run6','Run7','Run8','Run9','Run10', \
          #,'Run11',
            'Run14','Run14-A','Run14-A2','Run14-B','Run14-C','Run14-D','Run14-F','Run14-G']
legendlist=['Without CAM energy bug fix','','','','','','','','','', \
            'With CAM energy bug fix','','','','','','','','','','','','','','','','','','','','','','','']  

colorlist=[0,1,2,3,4,5,6,7,8,9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
linestylelist=[0,0,0,0,0,0,0,0,0,0, 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
regressionlist=[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1]
#
code=generalcode+'_ne16pg3'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout,regressionlist=regressionlist)
#
#
varXlist=['diagsumheatatm', 'diagsumheatatm'   ,'diagsumheatatm'   ,'diagsumheatatm'      ,'diagsumheatatm'         ,'diagsumheatatm'            ,'diagsumheatatm','diagsumheatatm', 'diagsumheatocn', 'diagsumheatsum'       ,'tempocn_trend'  ,'diagsumheatlnd','diagsumheatice','diagsumheatglc','diagsumheatatm','diagsumheatrof','LHFLXSHFLXFSNSFLNS']
varYlist=['diagsumheatocn', 'diagsumheatocnice','diagsumheatlndocn','diagsumheatlndocnice','diagsumheatlndocniceglc','diagsumheatlndrofocniceglc','diagsumheatlnd','FSLNT'         , 'tempocn_trend' , 'diagsumheatsumoffline','tempgaocn_trend','tempocn_trend' ,'tempocn_trend' ,'tempocn_trend' ,'tempocn_trend' ,'tempocn_trend' ,'diagsumheatatm'    ]
nvar=len(varXlist)
typevarXlist=['glob']*nvar
typevarYlist=['glob']*nvar

#loopanalysescatter2.loopanalysescatter2(\
#        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
#        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
#        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout)

# 1.b ne16pg3 - nhist
#----------------------------------
# x-axis
description='varcommon-typevarcommon'
expXlist=[\
          'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118', \
          'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118', \
          'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118', \
          'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118', \
          'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118', \
          'nhist.ne16pg3_tn14.nhist_cmip7.constLU.20260118', \
#
          'nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260225', \
#
          'nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260311', \
          'nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260311', \
          'nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260311']


#
refXlist=expXlist
 #
expXyear0list=[1850,1880,1910,1940,1970,2000,1850,1880,1910,1940]
expXyear1list=[1879,1909,1939,1979,1999,2013,1879,1909,1939,1979]
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
wXlist=[1.,0.]
# y-axis
expYlist=expXlist
refYlist=refXlist
expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=wXlist

# variables
varXlist=['FSLNT']
typevarXlist=['glob']
varYlist=['tempocn_trend']
typevarYlist=['glob']
# 
legendlist=[ \
            'historical (1850-2013, 30-year blocks)','','','','','', \
            'hist-esm (1850-1879, 30-year blocks, SE output)','','','']
colorlist=[0,0,0,0,0,0,1,1,1,1]
linestylelist=[0,0,0,0,0,0,0,0,0,0]
#
code=generalcode+'_ne16pg3_hist'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout)
#
##############
# 2. ne30pg3 #
##############
#
# 2.a ne30pg3 - n1850
#----------------------------------
#
# x-axis
description=''
# 5th very much out of balance [excluded from regression]
expXlist=[\
          'n1850.ne30_tn14.noresm3_0_beta03a-run1_yr001.20251016', \
          'n1850.ne30_tn14.noresm3_0_beta03b-run1_yr001.20251021', \
          'n1850.ne30_tn14.noresm3_0_beta03b-run2_yr001.20251023', \
          'n1850.ne30_tn14.noresm3_0_beta03b-run2_yr031_eminatred.20251031', \
          'n1850.ne30_tn14.noresm3_0_beta04-run1_yr001.20251103', \
          'n1850.ne30_tn14.nor3_b05-rc1-run1_yr001.20251110', \
          'n1850.ne30_tn14.noresm3_0_beta06-run1_yr001.20251114', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr001.20251223', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr031.20251227', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr051_cplhist.20251230', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218_lowmicromgautoconlwpexp', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218_highmicromgautoconlwpexp', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09.CESM3devTuning.20251220', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09.CESM3devTuning.v2.20251222', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001_lowdp1', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001_highdp1', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run1_yr001.20260213', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run2_yr001.20260213', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run3_yr001.20260226', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run1_yr101.20260120', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run2_yr101.20260120', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run3_yr101.20260123', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run4_yr101.20260126', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run5_yr121.20260127', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run6_yr121.20260128', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run7_yr121.20260128', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run8_yr121.20260131', \
          'n1850.ne30pg3_tn14.noresm3_0_beta18.20260530', \
          'n1850.ne30pg3_tn14.noresm3_0_beta18.20260606', \
          'n1850.ne30pg3_tn14.noresm3_0_beta18.egc_1p5.20260612', \
          'N1850.ne30pg3_tn14.noresm3_0_beta19-run13_yr151.20260618', \
          'N1850.ne30pg3_tn14.noresm3_0_beta20-run13_yr151.20260619', \
          'N1850.ne30pg3_tn14.noresm3_0_beta20-run13_yr151.20260626', \
          'N1850.ne30pg3_tn14.noresm3_0_beta20-run14_yr151.20260630', \
          'N1850.ne30pg3_tn14.noresm3_0_beta21-run1_yr101.20260711', \
          'N1850.ne30pg3_tn14.noresm3_0_beta21-run2_yr101.20260711', \
          'N1850.ne30pg3_tn14.noresm3_0_beta21-run3_yr101.20260711', \
          \
          'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316']
#
nexpid=len(expXlist)

refXlist=expXlist
 #
expXyear0list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year0')
expXyear1list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year1')
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA']*nexpid
wXlist=[1.,0.]
# y-axis
expYlist=expXlist
refYlist=refXlist
expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=wXlist

# variables
varXlist=['FSLNT']*nexpid
typevarXlist=['glob']*nexpid
varYlist=['tempocn_trend']*(nexpid-1)+['thetaogaocn_trend']
typevarYlist=['glob']*nexpid
# 
legendlist=['']*(nexpid-1)+['CESM3 (#316)']
legendlist=['Without CAM energy bug fix','','','','','','','','','','','','','','','','','','','','','','','','','','','', \
            'With bug fix (b18)','With bug fix (b18)','With bug fix (b18)','With bug fix (b19, spunup land)','With bug fix (b20, spunup land)','With bug fix (b20, spunup land)','With bug fix (b20, spunup land)','With bug fix (b21, spunup land)','With bug fix (b21, spunup land)','With bug fix (b21, spunup land)', \
            'CESM3 (#316)']

colorlist=np.arange(0,nexpid)
linestylelist=[0]*(nexpid-11) + [6,6,6,6,6,6,6,6,6,6,2]
regressionlist=[0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,1,1,1,1,1,1,1,-1]

#
code=generalcode+'_ne30pg3'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout,regressionlist=regressionlist)
#
#
# 2.b ne30pg3
#----------------------------------
# x-axis
description='varcommon-typevarcommon'
expXlist=[\
          'n1850.ne30_tn14.noresm3_0_beta03a-run1_yr001.20251016', \
#          'n1850.ne30_tn14.noresm3_0_beta03b-run1_yr001.20251021', \ does not exist anymore
          'n1850.ne30_tn14.noresm3_0_beta03b-run2_yr001.20251023', \
          'n1850.ne30_tn14.noresm3_0_beta03b-run2_yr031_eminatred.20251031', \
#          'n1850.ne30_tn14.nor3_b05-rc1-run1_yr001.20251110', \ does not exist anymore
          'n1850.ne30_tn14.noresm3_0_beta06-run1_yr001.20251114', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr001.20251223', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr031.20251227', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr051_cplhist.20251230', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218_lowmicromgautoconlwpexp', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218_highmicromgautoconlwpexp', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09.CESM3devTuning.20251220', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09.CESM3devTuning.v2.20251222', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001_lowdp1', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001_highdp1', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run1_yr001.20260213', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run2_yr001.20260213', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run3_yr001.20260226', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run1_yr101.20260120', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run2_yr101.20260120', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run3_yr101.20260123', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run4_yr101.20260126', \
#          'n1850.ne30pg3_tn14.noresm3_0_beta10-run5_yr121.20260127', \ does not exist anymore
#          'n1850.ne30pg3_tn14.noresm3_0_beta10-run6_yr121.20260128', \ does not exist anymore
#          'n1850.ne30pg3_tn14.noresm3_0_beta10-run7_yr121.20260128', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run8_yr121.20260131', \
          'n1850.ne30pg3_tn14.noresm3_0_beta18.20260530', \
          'n1850.ne30pg3_tn14.noresm3_0_beta18.20260606', \
          'n1850.ne30pg3_tn14.noresm3_0_beta18.egc_1p5.20260612']
#
nexpid=len(expXlist)

refXlist=expXlist
 #
expXyear0list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year0')
expXyear1list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year1')
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA']*nexpid
wXlist=[1.,0.]
# y-axis
expYlist=expXlist
refYlist=refXlist
expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=wXlist

# 
legendlist=['']*nexpid
colorlist=np.arange(0,nexpid)
linestylelist=[0]*(nexpid-3) + [6,6,6]


#varXlist=['diagsumheatatm', 'diagsumheatatm'   ,'diagsumheatatm'   ,'diagsumheatatm'      ,'diagsumheatatm'         ,'diagsumheatatm'            ,'diagsumheatatm','diagsumheatatm', 'diagsumheatocn', 'diagsumheatsum'       ,'tempocn_trend']
#varYlist=['diagsumheatocn', 'diagsumheatocnice','diagsumheatlndocn','diagsumheatlndocnice','diagsumheatlndocniceglc','diagsumheatlndrofocniceglc','diagsumheatlnd','FSLNT'         , 'tempocn_trend' , 'diagsumheatsumoffline','tempgaocn_trend']
#varXlist=['diagsumheatatm', 'diagsumheatatm'   ,'diagsumheatatm'   ,'diagsumheatatm'      ,'diagsumheatatm'         ,'diagsumheatatm'            ,'diagsumheatatm','diagsumheatatm', 'diagsumheatocn', 'diagsumheatsum'       ,'tempocn_trend'  ,'diagsumheatlnd','diagsumheatice','diagsumheatglc','diagsumheatatm','diagsumheatrof']
#varYlist=['diagsumheatocn', 'diagsumheatocnice','diagsumheatlndocn','diagsumheatlndocnice','diagsumheatlndocniceglc','diagsumheatlndrofocniceglc','diagsumheatlnd','FSLNT'         , 'tempocn_trend' , 'diagsumheatsumoffline','tempgaocn_trend','tempocn_trend' ,'tempocn_trend' ,'tempocn_trend' ,'tempocn_trend' ,'tempocn_trend' ]
varXlist=['hflxocn']
varYlist=['tempocn_trend']

nvar=len(varXlist)
typevarXlist=['glob']*nvar
typevarYlist=['glob']*nvar

loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout)



#################
# 3. NorESM2-LM #
#################
#
# x-axis
description='varcommon-typevarcommon'
expXlist=[\
          'N1850_f19_tn14_20190621', \
          'N1850_f19_tn14_20190722', \
          'N1850_f19_tn14_20190802', \
          'NHIST_f19_tn14_20190625', \
          'NHIST_f19_tn14_20190710', \
          'N1850ghgonly_f19_tn14_20190712', \
          'NCO2x4_f19_tn14_20190624', \
          'NCO2x4_f19_tn14_20190705', \
          'NCO2x4_f19_tn14_20190724']
#
nexpid=len(expXlist)

refXlist=expXlist
 #
expXyear0list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year0')
expXyear1list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year1')
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA']*nexpid
wXlist=[1.,0.]
# y-axis
expYlist=expXlist
refYlist=refXlist
expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=wXlist

# variables
varXlist=['FSLNT']
typevarXlist=['glob']
varYlist=['tempocn_trend']
typevarYlist=['glob']
# 
legendlist=['piControl (0-200)', \
            'piControl (201-300)', \
            'piControl (301-500)',
            'historical (1850-1949)', \
            'historical (1950-2014)', \
            'hist-GHG (1850-2014)', \
            'abrupt-4xCO2 (1-120)', \
            'abrupt-4xCO2 (121-150)', \
            'abrupt-4xCO2 (151-500)']
            
colorlist=np.arange(0,nexpid)
linestylelist=[0]*nexpid
#
code=generalcode+'_NorESM2-LM'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout)
#
#################
# 4. NorESM2-MM #
#################
#
# x-axis
description='varcommon-typevarcommon'
expXlist=[\
          'N1850frc2_f09_tn14_20191001', \
          'N1850frc2_f09_tn14_20191012', \
          'N1850frc2_f09_tn14_20191113', \
          'NHISTfrc2_f09_tn14_20191001', \
          'NHISTfrc2_f09_tn14_20191025']
#
nexpid=len(expXlist)

refXlist=expXlist
 #
expXyear0list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year0')
expXyear1list=expidlist2attributelist.expidlist2attributelist(expidlist=expXlist,attributetype='year1')
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA']*nexpid
wXlist=[1.,0.]
# y-axis
expYlist=expXlist
refYlist=refXlist
expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=wXlist

# variables
varXlist=['FSLNT']
typevarXlist=['glob']
varYlist=['tempocn_trend']
typevarYlist=['glob']
# 
legendlist=['piControl (1-100)', \
            'piControl (101-250)', \
            'piControl (251-500)', \
            'historical (1850-1949)', \
            'historical (1950-2014']
colorlist=np.arange(0,nexpid)
linestylelist=[0]*nexpid
#
code=generalcode+'_NorESM2-MM'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout)
#

#################
# 5. CESM - 316 #
#################
#
# x-axis
description='varcommon-typevarcommon'
expXlist=[\
          'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316', \
          'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316', \
          'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316', \
          'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316', \
          'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316', \
          'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316']
#
nexpid=len(expXlist)

refXlist=expXlist
 #
#expXyear0list=[70,75,80,85,90,95]
#expXyear1list=[74,79,84,89,94,99]
expXyear0list=[70]*6
expXyear1list=[99]*6
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA']*nexpid
wXlist=[1.,0.]
# y-axis
expYlist=expXlist
refYlist=refXlist
expYyear0list=expXyear0list
expYyear1list=expXyear1list
refYyear0list=expXyear0list
refYyear1list=expXyear1list
seasonYlist=seasonXlist
wYlist=wXlist

# variables
varXlist=['FSLNT']
typevarXlist=['glob']
varYlist=['thetaogaocn_trend']
typevarYlist=['glob']
# 
legendlist=['(70-74)', \
            '(75-79)', \
            '(80-84)', \
            '(85-89)', \
            '(90-94)', \
            '(95-99)', \
              ]
colorlist=np.arange(0,nexpid)
linestylelist=[0]*nexpid
#
code=generalcode+'_CESM3_316'

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout)
#


