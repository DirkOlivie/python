import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='typevarcommon'
figlayout=cfiglayout.CFigLayout(legendlocation='',xrange=[2015,2100])
#figlayout=cfiglayout.CFigLayout(legendlocation='')
# 
# 1. NSSP534frc2esm
#------------------------------------------
#expidlist=['N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027', \
#           'N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027', \
#           'N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027', \
#           'N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027']
#
expidlist=['N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm']
#           'N1850_f19_tn14_20190730esm', \
#           'N1850_f19_tn14_20190730esm', \
#           'N1850_f19_tn14_20190730esm', \
#           'N1850_f19_tn14_20190730esm']
#
#expidlist=['n1850esm.ne30_tn14.hybrid.3.0a01.20250410', \
#           'n1850esm.ne30_tn14.hybrid.3.0a01.20250410', \
#           'n1850esm.ne30_tn14.hybrid.3.0a01.20250410', \
#           'n1850esm.ne30_tn14.hybrid.3.0a01.20250410']
#
expidlist=['NSSP534frc2esm_f19_tn14_20230106ext', \
           'NSSP534frc2esm_f19_tn14_20230106ext', \
           'NSSP534frc2esm_f19_tn14_20230106ext', \
           'NSSP534frc2esm_f19_tn14_20230106ext', \
           'NSSP534frc2esm_f19_tn14_20230106ext']

expidlist=['NSSP534frc2esm_f19_tn14_20230106', \
           'NSSP534frc2esm_f19_tn14_20230106', \
           'NSSP534frc2esm_f19_tn14_20230106', \
           'NSSP534frc2esm_f19_tn14_20230106', \
           'NSSP534frc2esm_f19_tn14_20230106']




refidlist=expidlist
#
wlist=[1.,0.]
#
variablegrouplist=[ \
#                   ['TMCO2','TMCO2_FFF','TMCO2_LND','TMCO2_OCN','TMCO2_FFFLNDOCN'], \
#                   ['SFCO2','SFCO2_FFF','SFCO2_LND','SFCO2_OCN','SFCO2_FFFLNDOCN'], \
#                   ['TMCO2_trend','TMCO2_FFF_trend','TMCO2_LND_trend','TMCO2_OCN_trend','TMCO2_FFFLNDOCN_trend'], \
                   ['TMCO2_offset','TMCO2_FFF_offset','TMCO2_LND_offset','TMCO2_OCN_offset','TMCO2_FFFLNDOCN_offset'], \
                   ['SFCO2_ac_CO2_columnburden_cumulative','SFCO2_FFF_ac_CO2_columnburden_cumulative','SFCO2_LND_cumulative','SFCO2_OCN_cumulative','SFCO2_FFFLNDOCN_ac_CO2_columnburden_cumulative']]

#              'CO2_columnburden','CO2_FFF_columnburden','CO2_LND_columnburden','CO2_OCN_columnburden']
smoothlist=[0,0,0,0,0]
#smoothlist=[5,5,5,5]#,5,5,5,5]
#
colorlist=[0,1,2,3,4]#,4,5,6,7]
#            
shiftlist=[0,0,0,0,0]#,0,0,0,0]
#
code='n20250429_co2_jerry'
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for variablelist in variablegrouplist:
#
    legendlist=variablelist
    for freqtype in freqtypelist : 
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)


# 2. NSSP534frc2esm
#------------------

expidlist=['NSSP534frc2esm_f19_tn14_20230106ext', \
           'NSSP534frc2esm_f19_tn14_20230106ext']

refidlist=expidlist
#
wlist=[1.,0.]
#
variablegrouplist=[['SFCO2','TMCO2_trend'], \
                   ['SFCO2_FFF','TMCO2_FFF_trend'], \
                   ['SFCO2_LND','TMCO2_LND_trend'], \
                   ['SFCO2_OCN','TMCO2_OCN_trend'], \
                   ['SFCO2_FFFLNDOCN','TMCO2_FFFLNDOCN_trend']]

smoothlist=[0,0]
#
colorlist=[0,1]
#            
shiftlist=[0,0]
#
code='n20250429_co2_jerry_trend'
#
typevarlist=['glob']
freqtypelist=['YEA']
#
#for variablelist in variablegrouplist:
#
#    legendlist=variablelist
#    for freqtype in freqtypelist : 
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)




# 3. TMCO2 and SFCO2_cumulative : in same figure
#    TMCO2_trend and SFCO2      : in same figure
#-----------------------------------------------
#
expidgrouplist=[\
#                ['N1850_f19_tn14_20190730esm'] * 10, \
                ['NSSP534frc2esm_f19_tn14_20230106ext'] * 10, \
                ['NSSP585_f19_tn14_20191223esm'] * 10, \
#                ['NHIST_f19_tn14_20191104esm'] * 10, \
#                ['N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027']*10, \
#                ['n1850esm.ne30_tn14.hybrid.3.0a01.20250410']*10, \
#                ['n1850esm.ne16_tn14.nor3_b03_20250926']*10] 
                ['n1850esm.ne16_tn14.2xssp534co2emissfiles.nor3_b03b_co2refactor_20251105']*10]
                                 
for expidlist in expidgrouplist :  

    refidlist=expidlist
#
    wlist=[1.,0.]
#
    variablegrouplist=[['TMCO2_FFF_offset','TMCO2_LND_offset','TMCO2_OCN_offset','TMCO2_FFFLNDOCN_offset','TMCO2_offset', \
                        'SFCO2_FFF_cumulative','SFCO2_LND_cumulative','SFCO2_OCN_cumulative','SFCO2_FFFLNDOCN_cumulative','SFCO2_cumulative'], \
                       ['TMCO2_FFF_trend','TMCO2_LND_trend','TMCO2_OCN_trend','TMCO2_FFFLNDOCN_trend','TMCO2_trend', \
                        'SFCO2_FFF','SFCO2_LND','SFCO2_OCN','SFCO2_FFFLNDOCN','SFCO2']]

    smoothlist=[0,0,0,0,0,0,0,0,0,0]
    colorlist=[1,2,0,3,4,1,2,0,3,4]
    shiftlist=[0,0,0,0,0,0,0,0,0,0]
    linestylelist=[0,0,0,0,0,1,1,1,1,1]
#
    code='n20250429_co2_jerry'
#
    typevarlist=['glob']
    freqtypelist=['YEA','monthly']
#
    code='n20250429_co2_jerry_combined_'+expidlist[0]
#
    for variablelist in variablegrouplist:

        legendlist=variablelist
        for freqtype in freqtypelist : 
            loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



# 3. TMCO2 and SFCO2_cumulative : in same figure
#    TMCO2_trend and SFCO2      : in same figure
#-----------------------------------------------
#
expidgrouplist=[\
                ['NSSP534frc2esm_f19_tn14_20230106'] * 10 ]
                                 
for expidlist in expidgrouplist :  

    refidlist=expidlist
#
    wlist=[1.,0.]
#
    variablegrouplist=[['TMCO2_FFF_offset','TMCO2_LND_offset','TMCO2_OCN_offset','TMCO2_FFFLNDOCN_offset','TMCO2_offset', \
                        'SFCO2_FFF_ac_CO2_columnburden_cumulative','SFCO2_LND_cumulative','SFCO2_OCN_cumulative','SFCO2_FFFLNDOCN_ac_CO2_columnburden_cumulative','SFCO2_ac_CO2_columnburden_cumulative']]

    smoothlist=[0,0,0,0,0,0,0,0,0,0]
    colorlist=[1,2,0,3,4,1,2,0,3,4]
    shiftlist=[0,0,0,0,0,0,0,0,0,0]
    linestylelist=[0,0,0,0,0,1,1,1,1,1]
#
    code='n20250429_co2_jerry'
#
    typevarlist=['glob']
    freqtypelist=['YEA','monthly']
#
    code='n20250429_co2_jerry_combined_'+expidlist[0]
#
    for variablelist in variablegrouplist:

        legendlist=variablelist
        for freqtype in freqtypelist : 
            loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)






# 4. TMCO2_offset and TMCO2_trend : in different figures
#-----------------------------------------------------
#
expidgrouplist=[\
#                ['N1850_f19_tn14_20190730esm'] * 5, \
#                ['NSSP534frc2esm_f19_tn14_20230106ext'] * 5, \
#                ['NHIST_f19_tn14_20191104esm'] * 5, \
#                ['N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027']*5, \
                ['n1850esm.ne16_tn14.2xssp534co2emissfiles.nor3_b03b_co2refactor_20251105']*5]

for expidlist in expidgrouplist :

    refidlist=expidlist
#
    wlist=[1.,0.]
#
    variablegrouplist=[['TMCO2_FFF_offset','TMCO2_LND_offset','TMCO2_OCN_offset','TMCO2_FFFLNDOCN_offset','TMCO2_offset'], \
                       ['TMCO2_FFF_trend','TMCO2_LND_trend','TMCO2_OCN_trend','TMCO2_FFFLNDOCN_trend','TMCO2_trend']]

    smoothlist=[0,0,0,0,0]
    colorlist=[1,2,0,3,4]
    shiftlist=[0,0,0,0,0]
    linestylelist=[0,0,0,0,0]
#
    code='n20250429_co2_jerry'
#
    typevarlist=['glob']
    freqtypelist=['YEA']
#
    code='n20250429_co2_jerry_combinedTM_'+expidlist[0]
#
    for variablelist in variablegrouplist:

        legendlist=variablelist
        for freqtype in freqtypelist :
            loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


# 5. SFCO2_cumulative and SFCO2 : 
#------------------------------------------
#
expidgrouplist=[\
#                ['N1850_f19_tn14_20190730esm'] * 5, \
#                ['NSSP534frc2esm_f19_tn14_20230106ext'] * 5, \
#                ['NHIST_f19_tn14_20191104esm'] * 5, \
#                ['N1850frc2esm_DMS_noBio_noRiv_f19_tn14_20231027']*5, \
                ['n1850esm.ne16_tn14.2xssp534co2emissfiles.nor3_b03b_co2refactor_20251105']*5 , \
                ['n1850esm.ne16_tn14.2xssp534co2emissfiles.nor3_b03b_co2refactor_20251112']*5 ]

for expidlist in expidgrouplist :

    refidlist=expidlist
#
    wlist=[1.,0.]
#
    variablegrouplist=[['SFCO2_FFF_cumulative','SFCO2_LND_cumulative','SFCO2_OCN_cumulative','SFCO2_FFFLNDOCN_cumulative','SFCO2_cumulative'], \
                       ['SFCO2_FFF','SFCO2_LND','SFCO2_OCN','SFCO2_FFFLNDOCN','SFCO2']]

    smoothlist=[0,0,0,0,0]
    colorlist=[1,2,0,3,4]
    shiftlist=[0,0,0,0,0]
    linestylelist=[1,1,1,1,1]
#
    typevarlist=['glob']
    freqtypelist=['YEA']
#
    code='n20250429_co2_jerry_combinedSFcumul_'+expidlist[0]
#
    for variablelist in variablegrouplist:

        legendlist=variablelist
        for freqtype in freqtypelist :
            loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# 6. ada SFCO2_FFF
#-----------------
figlayout=cfiglayout.CFigLayout(legendlocation='',xrange=[2015,2021])
expidlist=['n1850esm.ne16_tn14.2xssp534co2emissfiles.nor3_b03b_co2refactor_20251112']
refidlist=expidlist
#
wlist=[1.,0.]
#
variablelist=['SFCO2_FFF_as_C']

smoothlist=[0]
colorlist=[1]
shiftlist=[0]
linestylelist=[0]
legendlist=variablelist
#
typevarlist=['glob']
freqtypelist=['YEA']
#
code='n20250429_co2_jerry_ada'
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)




