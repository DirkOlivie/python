import loopanalysescatter2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist

# MAIN PROGRAM
# CORRECTION
#   2024-11-24 : replaced NorESM2-LM_pdClim-controlfixO3-2050ssp370_r1i1p1f1_gn by NorESM2-LM_pdClim-controlfixO3-2050ssp370noAER_r1i1p1f1_gn



description='varcommon-typevarcommon'
generalcode='n20250319_navigate_geoeng'

figlayout=cfiglayout.CFigLayout('')

# 1. REFERENCE EXPERIMENTS
#----------------------------------
# x-axis
expXlist=[ \
           'N1850_f19_tn14_20250311_test01', \
           'N1850_f19_tn14_20250311_test06', \
           'N1850_f19_tn14_20250311_test05', \
           'N1850_f19_tn14_20250311_test02', \
           'N1850_f19_tn14_20250311_test03', \
           'N1850_f19_tn14_20250311_test04', \
            \
           'N1850_f19_tn14_20250311_test06', \
           'N1850_f19_tn14_20250311_test05', \
           'N1850_f19_tn14_20250311_test02']
#
refXlist=[ \
           'N1850_f19_tn14_20250311_test01', \
           'N1850_f19_tn14_20250311_test01', \
           'N1850_f19_tn14_20250311_test01', \
           'N1850_f19_tn14_20250311_test01', \
           'N1850_f19_tn14_20250311_test01', \
           'N1850_f19_tn14_20250311_test01', \
            \
           'N1850_f19_tn14_20250311_test01', \
           'N1850_f19_tn14_20250311_test01', \
           'N1850_f19_tn14_20250311_test01']
 #
expXyear0list=[1605,1605,1605,1605,1605,1605,1615,1615,1615]
expXyear1list=[1609,1609,1609,1609,1609,1609,1619,1619,1619]
refXyear0list=expXyear0list
refXyear1list=expXyear1list
seasonXlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA','YEA']
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
varXlist=['EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2','EMI_SO2SO4_as_SO2_TOT_noresm2']
typevarXlist=['glob','glob','glob','glob','glob','glob']
varYlist=['AOD_VISdivDAYFOC','cb_SULFATE','TREFHT','PRECT','TREFHT','mmflxdmax26.0Nocn']
typevarYlist=['glob','glob','glob','glob','60N90N','atlarc']
# 
legendlist=[ \
            '0 Tg[S] yr'+r'$^{-1}$ (year 6--10)', \
            '2 Tg[S] yr'+r'$^{-1}$ (year 6--10)', \
            '5 Tg[S] yr'+r'$^{-1}$ (year 6--10)', \
            '10 Tg[S] yr'+r'$^{-1}$ (year 6--10)', \
            '20 Tg[S] yr'+r'$^{-1}$ (year 6--10)', \
            '50 Tg[S] yr'+r'$^{-1}$ (year 6--10)', \
            '2 Tg[S] yr'+r'$^{-1}$ (year 16--20)', \
            '5 Tg[S] yr'+r'$^{-1}$ (year 16--20)', \
            '10 Tg[S] yr'+r'$^{-1}$ (year 16--20)']
colorlist=[1,2,3,4,5,6,2,3,4]
linestylelist=[0,0,0,0,0,0,1,1,1]
#
code=generalcode

#
loopanalysescatter2.loopanalysescatter2(\
        expXlist=expXlist,refXlist=refXlist,expXyear0list=expXyear0list,expXyear1list=expXyear1list,refXyear0list=refXyear0list,refXyear1list=refXyear1list,seasonXlist=seasonXlist,wXlist=wXlist,varXlist=varXlist,typevarXlist=typevarXlist, \
        expYlist=expYlist,refYlist=refYlist,expYyear0list=expYyear0list,expYyear1list=expYyear1list,refYyear0list=refYyear0list,refYyear1list=refYyear1list,seasonYlist=seasonYlist,wYlist=wYlist,varYlist=varYlist,typevarYlist=typevarYlist, \
        legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist,description=description,code=code,figlayout=figlayout)

