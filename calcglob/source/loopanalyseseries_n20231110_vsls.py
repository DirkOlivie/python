import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

typevar='glob'
typevarlist=['glob']
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# FULLY COUPLED SIMULATIONS
#--------------------------
expidlist=[ \
            'NHIST_f19_tn14_20190625ext', \
            'NSSP126frc2_f19_tn14_20191014', \
            'NSSP245frc2_f19_tn14_20191014', \
            'NSSP370frc2_f19_tn14_20191014', \
            'NSSP585frc2_f19_tn14_20191014', \
            'N1850_f19_tn14_20190621ext',\
            'NCO2x4_f19_tn14_20190624ext']   
#       
refidlist=expidlist
#
wlist=[1.,0.]
#
#
legendlist=['historical', \
            'ssp1-2.6', \
            'ssp2-4.5', \
            'ssp3-7.0', \
            'ssp5-8.5', \
            'piControl', \
            'abrupt-4xCO2']
#
smoothlist=[0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,1850-1600,1850-1]
#
colorlist=[0,1,2,3,4,5,6]
#
variablelist=['FSDSC','co2vmr','TREFHT','TMQ','Q_columnburden']
#
code='n20231110_vsls'
#
figlayout=cfiglayout.CFigLayout()
#
for typevar in typevarlist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# FULLY COUPLED SIMULATIONS (without 1850-1949)
#--------------------------
expidlist=[ \
            'NHIST_f19_tn14_20190710', \
            'NSSP126frc2_f19_tn14_20191014', \
            'NSSP245frc2_f19_tn14_20191014', \
            'NSSP370frc2_f19_tn14_20191014', \
            'NSSP585frc2_f19_tn14_20191014', \
            'N1850_f19_tn14_20190722',\
            'NCO2x4_f19_tn14_20190724']
#       
refidlist=expidlist
#
wlist=[1.,0.]
#
#
legendlist=['historical', \
            'ssp1-2.6', \
            'ssp2-4.5', \
            'ssp3-7.0', \
            'ssp5-8.5', \
            'piControl', \
            'abrupt-4xCO2']
#
smoothlist=[0,0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,1850-1600,1850-1]
#
colorlist=[0,1,2,3,4,5,6]
#
variablelist=['T200','T500']
#
code='n20231110_vsls'
#
figlayout=cfiglayout.CFigLayout()
#
for typevar in typevarlist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)



# FIXED-SST SIMULATIONS
#----------------------
expidlist=[ \
            'NF1850norbc_f19_20191025', \
            'NF1850norbc_4xco2_f19_20191025', \
            'NF1850norbc_2xco2_f19_20191025', \
            'NF1850norbc_co22014_f19_20191025', \
            'NF1850norbc_ch42014_f19_20191025', \
            'NF1850norbc_n2o2014_f19_20200908']
#       
refidlist=expidlist
#
wlist=[1.,0.]
#
#
legendlist=['piClim-control', \
            'piClim-4xCO2', \
            'piClim-2xCO2', \
            'piClim-CO2', \
            'piClim-CH4', \
            'piClim-N2O']
#
smoothlist=[0,0,0,0,0,0]
#            
shiftlist=[0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5]
#
variablelist=['FSDSC']
#
code='n20231110_vsls_fsst'
#
figlayout=cfiglayout.CFigLayout()
#
#for typevar in typevarlist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
