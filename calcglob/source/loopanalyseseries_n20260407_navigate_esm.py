import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'

# I. IMPOSE SIMULATIONS ALONE : absolute values
#----------------------------

code='n20250615_navigate_esm'
figlayout=cfiglayout.CFigLayout()

expidlist=[ \
           'N1850frc2esm_ZECMIP_B3_f19_tn14_20200316', \
           'N1850frc2esm_ZECMIP_B3_02_f19_tn14_20210224', \
           'N1850frc2esm_ZECMIP_B3_03_f19_tn14_20210224', \
            \
           'N1850frc2esm_IMPOSE_C1a_f19_tn14_20200316', \
           'N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224', \
           'N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224', \
            \
           'N1850frc2esm_ZECMIP_B4_f19_tn14_20200316', \
           'N1850frc2esm_ZECMIP_B4_02_f19_tn14_20210224', \
           'N1850frc2esm_ZECMIP_B4_03_f19_tn14_20210224']
#
refidlist=expidlist
wlist=[1.,0.]
#legendlist=[ \
#            'B3','','', \
#            'B3C1a','','', \
#            'B4','',''] 
legendlist=[ \
            'B3','B3','B3', \
            'B3C1a','B3C1a','B3C1a', \
            'B4','B4','B4'] 
#
smoothlist=[0,0,0,0,0,0,0,0,0]
colorlist=[0,0,0,1,1,1,2,2,2]
linestylelist=[0,0,0,0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0,0,0,0]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['TREFHT','PRECT','CLDTOT','PRECT','SFCO2_FFF','co2vmr','CO2_columnburden','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
variablelist=['CO2_columnburden_as_RF']
typevarlist=['glob']
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# atmosphere
variablelist=['TREFHT']
typevarlist=['60N90N']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



# amoc
#variablelist=['mmflxdmax26.0Nocn']
#typevarlist=['glob','atlarc']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)




# II. IMPOSE SIMULATIONS ALONE : differences
#-----------------------------

code='n20250615_navigate_esm_diff'
figlayout=cfiglayout.CFigLayout()

expidlist=[ \
           'N1850frc2esm_ZECMIP_B3_f19_tn14_20200316', \
           'N1850frc2esm_ZECMIP_B3_02_f19_tn14_20210224', \
           'N1850frc2esm_ZECMIP_B3_03_f19_tn14_20210224', \
            \
           'N1850frc2esm_IMPOSE_C1a_f19_tn14_20200316ext', \
           'N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224ext', \
           'N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224ext']
        
refidlist=[ \
           'N1850frc2esm_ZECMIP_B4_f19_tn14_20200316', \
           'N1850frc2esm_ZECMIP_B4_02_f19_tn14_20210224', \
           'N1850frc2esm_ZECMIP_B4_03_f19_tn14_20210224', \
            \
           'N1850frc2esm_ZECMIP_B4_f19_tn14_20200316', \
           'N1850frc2esm_ZECMIP_B4_02_f19_tn14_20210224', \
           'N1850frc2esm_ZECMIP_B4_03_f19_tn14_20210224']
#
wlist=[1.,-1.]
#legendlist=[ \
#            'B3-B4','','', \
#            'B3C1a-B4','','']
legendlist=[ \
            'B3-B4','B3-B4','B3-B4', \
            'B3C1a-B4','B3C1a-B4','B3C1a-B4']
#
smoothlist=[0,0,0,0,0,0]
colorlist=[0,0,0,1,1,1]
linestylelist=[0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['TREFHT','PRECT','CLDTOT','PRECT','SFCO2_FFF','co2vmr','CO2_columnburden','CO2_columnburden_as_vmr','CO2_columnburden_as_RF']
variablelist=['CO2_columnburden_as_RF']
typevarlist=['glob']
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# atmosphere
variablelist=['TREFHT']
typevarlist=['60N90N']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



# amoc
#variablelist=['mmflxdmax26.0Nocn']
#typevarlist=['glob','atlarc']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)









# III. IMPOSE SIMULATIONS + TEST SIMULATIONS
#-----------------------
code='n20250615_navigate_esm_geoeng'
figlayout=cfiglayout.CFigLayout(xrange=[1850,1950])

expidlist=[ \
           'N1850frc2esm_ZECMIP_B3_f19_tn14_20200316', \
           'N1850frc2esm_ZECMIP_B3_02_f19_tn14_20210224', \
           'N1850frc2esm_ZECMIP_B3_03_f19_tn14_20210224', \
            \
           'N1850frc2esm_IMPOSE_C1a_f19_tn14_20200316', \
           'N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224', \
           'N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224', \
            \
           'N1850frc2esm_ZECMIP_B4_f19_tn14_20200316', \
           'N1850frc2esm_ZECMIP_B4_02_f19_tn14_20210224', \
           'N1850frc2esm_ZECMIP_B4_03_f19_tn14_20210224', \
            \
           'N1850frc2esm_B3_r1890_0tg_f19_tn14_20250613', \
           'N1850frc2esm_B3_r1890_2tg_f19_tn14_20250613', \
           'N1850frc2esm_B3_r1910_2tg_f19_tn14_20250613']            
#
refidlist=expidlist
wlist=[1.,0.]
legendlist=[ \
            'B3','','', \
            'B3C1a','','', \
            'B4','','', \
            '0 Tg[S]/yr (1890)', \
            '2 Tg[S]/yr (1890)', \
            '2 Tg[S]/yr (1910)']     
#
smoothlist=[0,0,0,0,0,0,0,0,0,0,0,0]
colorlist=[0,0,0,1,1,1,2,2,2,3,4,5]
linestylelist=[0,0,0,0,0,0,0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0,0,0,0,0,0,0]
#
freqtypelist=['YEA']
#
# atmosphere
variablelist=['TREFHT','PRECT','CLDTOT','PRECT','SFCO2_FFF','co2vmr','CO2_columnburden']
typevarlist=['glob']
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# atmosphere
variablelist=['TREFHT']
typevarlist=['60N90N']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



# amoc
#variablelist=['mmflxdmax26.0Nocn']
#typevarlist=['glob','atlarc']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

code='n20250615_navigate_esm_geoeng_long'
figlayout=cfiglayout.CFigLayout()
# atmosphere
variablelist=['TREFHT','PRECT','CLDTOT','PRECT','SFCO2_FFF','co2vmr','CO2_columnburden']
typevarlist=['glob']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# atmosphere
variablelist=['TREFHT']
typevarlist=['60N90N']
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



# amoc
#variablelist=['mmflxdmax26.0Nocn']
#typevarlist=['glob','atlarc']
#for freqtype in freqtypelist :
#    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


