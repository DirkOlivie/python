import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


description='varcommon-typevarcommon'
generalcode='n20241202_methanemip'


# 1. INDIVIDUAL MEMBERS
#------------------------------------------------------------------------
#
expidlist=[ \
#          'NHIST_tropstratchem_01_f19_tn14_r1990_s01_20241118', \
           'NHIST_tropstratchem_01_f19_tn14_r2000_s01_20241118', \
           'NHIST_tropstratchem_02_f19_tn14_r2000_s01_20241118', \
           'NHIST_tropstratchem_03_f19_tn14_r2000_s01_20241118', \
           'NHIST_tropstratchem_04_f19_tn14_r2000_s01_20241118',\
           'NHIST_tropstratchem_05_f19_tn14_r2000_s01_20241118',\
           'NHIST_tropstratchem_06_f19_tn14_r2000_s01_20241118',\
           'NSSP245_tropstratchem_01_f19_tn14_s01_20241118', \
           'NSSP245_tropstratchem_02_f19_tn14_s01_20241118', \
           'NSSP245_tropstratchem_03_f19_tn14_s01_20241118', \
           'NSSP245_tropstratchem_04_f19_tn14_s01_20241118', \
           'NSSP245_tropstratchem_05_f19_tn14_s01_20241118', \
           'NSSP245_tropstratchem_06_f19_tn14_s01_20241118', \
           'NSSP245TECH_tropstratchem_01_f19_tn14_s01_20241118', \
           'NSSP245TECH_tropstratchem_02_f19_tn14_s01_20241118', \
           'NSSP245TECH_tropstratchem_03_f19_tn14_s01_20241118', \
           'NSSP245TECH_tropstratchem_04_f19_tn14_s01_20241118', \
           'NSSP245TECH_tropstratchem_05_f19_tn14_s01_20241118', \
           'NSSP245TECH_tropstratchem_06_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_01_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_02_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_03_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_04_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_05_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_06_f19_tn14_s01_20241118']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[\
#           '1990-1990', \
            '2000-2014','','','','','', \
            'SSP2-4.5','','','','','', \
            'SSP2-4.5-tech','','','','','', \
            'SSP2-4.5-amb','','','','','']
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#
shiftlist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#
colorlist=[0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]
#

# annual mean
variablelist=['CH4_SRF','SWCF','cb_O3','O3_SRF','TREFHT','PRECT','ICEFRAC']
typevarlist=['glob']
freqtype='YEA'
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# september - NH 
variablelist=['ICEFRAC']
typevarlist=['NH']
freqtype='SEP'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# september - NH
variablelist=['ICEFRAC']
typevarlist=['NH']
freqtype='YEA'
#
#loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# 2. ENSEMBLE MEAN
#------------------------------------------------------------------------
#
expidlist=[ \
#          'NHIST_tropstratchem_01_f19_tn14_r1990_s01_20241118', \
           'NHISTSSP245_tropstratchem_123456_f19_tn14_r2000_s01_20241118', \
           'NSSP245TECH_tropstratchem_123456_f19_tn14_s01_20241118', \
           'NSSP245AMBI_tropstratchem_123456_f19_tn14_s01_20241118']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=[\
#           '1990-1990', \
            'historical+SSP2-4.5', \
            'SSP2-4.5-tech', \
            'SSP2-4.5-amb']
#
smoothlist=[0,0,0]
#
shiftlist=[0,0,0]
#
colorlist=[0,1,2]
#
ensembletypelist=['minmax','minmax','minmax']

# annual mean
variablelist=['CH4_SRF','SWCF','cb_O3','O3_SRF','TREFHT','PRECT','ICEFRAC']
typevarlist=['glob']
freqtype='YEA'
#
code=generalcode
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,ensembletypelist=ensembletypelist)

# september - NH 
variablelist=['ICEFRAC']
typevarlist=['NH']
freqtype='SEP'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,ensembletypelist=ensembletypelist)

# september - NH
variablelist=['ICEFRAC']
typevarlist=['NH']
freqtype='YEA'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,ensembletypelist=ensembletypelist)
