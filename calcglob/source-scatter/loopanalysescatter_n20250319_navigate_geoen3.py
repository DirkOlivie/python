import loopanalysescatter2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist

# MAIN PROGRAM
# CORRECTION
#   2024-11-24 : replaced NorESM2-LM_pdClim-controlfixO3-2050ssp370_r1i1p1f1_gn by NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn



description='varcommon-typevarcommon'
generalcode='n20250319_navigate_geoeng3'

figlayout=cfiglayout.CFigLayout('')

# 1. REFERENCE EXPERIMENTS
#----------------------------------
# x-axis
expXlist=[ \
           'NF1850norbc_f19_20250311_test01', \
           'NF1850norbc_f19_20250311_test06', \
           'NF1850norbc_f19_20250311_test05']
#
refXlist=[ \
           'NF1850norbc_f19_20250311_test01', \
           'NF1850norbc_f19_20250311_test01', \
           'NF1850norbc_f19_20250311_test01']
 #
expXyear0list=[5,5,5]
expXyear1list=[25,25,25]
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA','YEA','YEA']
wXlist=[1.,-1.]
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
varXlist=['EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2']
typevarXlist=['glob','glob','glob','glob','glob']
varYlist=['AOD_VISdivDAYFOC','cb_SULFATE','TREFHT','PRECT','FSLNT']
typevarYlist=['glob','glob','glob','glob','glob']
# 
legendlist=[ \
            '0 Tg[S] yr'+r'$^{-1}$ (year 5--30)', \
            '2 Tg[S] yr'+r'$^{-1}$ (year 5--30)', \
            '5 Tg[S] yr'+r'$^{-1}$ (year 5--30)']
colorlist=[1,2,3]
linestylelist=[0,0,0]
#
code=generalcode

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout)

