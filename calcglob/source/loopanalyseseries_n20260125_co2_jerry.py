import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'
figlayout=cfiglayout.CFigLayout(legendlocation='')
# 
# OUTPUT ON SE GRID

#   JERRY, DIRK1, DIRK2, ADA
#------------------------------------------
expidlist=['n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120', \
           'n1850esm.ne16pg3_tn4.noresm3_0_beta10.atmco2fluxzero.20260120', \
           'n1850esm.ne16pg3_tn4.noresm3_0_beta10.atmco2fluxzero.20260121', \
           'n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.co2_surfacefossilfuelemis_only.20260120']

refidlist=expidlist
#
wlist=[1.,0.]
#
variablelist=['TMCO2','TMCO2_FFF','TMCO2_LND','TMCO2_OCN','TMCO2_FFFLNDOCN', \
              'SFCO2','SFCO2_FFF','SFCO2_LND','SFCO2_OCN','SFCO2_FFFLNDOCN', \
              'TMCO2_trend','TMCO2_FFF_trend','TMCO2_LND_trend','TMCO2_OCN_trend','TMCO2_FFFLNDOCN_trend', \
              'TMCO2_offset','TMCO2_FFF_offset','TMCO2_LND_offset','TMCO2_OCN_offset','TMCO2_FFFLNDOCN_offset', \
              'SFCO2_cumulative','SFCO2_FFF_cumulative','SFCO2_LND_cumulative','SFCO2_OCN_cumulative','SFCO2_FFFLNDOCN_cumulative']

legendlist=['Jerry','Dirk1','Dirk2','Ada']

shiftlist=[-250,-250,-250,-2014]

smoothlist=[0,0,0,0]
#
colorlist=[0,1,2,3]
#            
code='n20260125_co2_jerry_overview'
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
#






# DIRK2
# ------------------------------------------
expidlist=['n1850esm.ne16pg3_tn4.noresm3_0_beta10.atmco2fluxzero.20260121']

refidlist=expidlist
#
wlist=[1.,0.]
#
variablelist=['TMCO2']

legendlist=['Dirk2']

shiftlist=[-250]

smoothlist=[0]
#
colorlist=[2]
#            
code='n20260125_co2_jerry_atmco2fluxzero'
#
typevarlist=['glob']
freqtypelist=['YEA','monthly']
#
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# ADA
#----------------------------------
description='typevarcommon'

expidgrouplist=[\
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120'] * 5, \
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120huit'] * 5, \
                ['n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.co2_surfacefossilfuelemis_only.20260120'] * 5, \
                ['n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.co2_aircraftemis_only.20260120'] * 5, \
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10.lndco2fluxonlypos.20260127'] * 5, \
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10.lndco2fluxonlyneg.20260127' ] * 5 ]

for expidlist in expidgrouplist :

    refidlist=expidlist
#
    wlist=[1.,0.]
#
    variablegrouplist=[['SFCO2_FFF','SFCO2_LND','SFCO2_OCN','SFCO2_FFFLNDOCN','SFCO2'], \
                       ['TMCO2_FFF','TMCO2_LND','TMCO2_OCN','TMCO2_FFFLNDOCN','TMCO2'], \
                       ['TMCO2_FFF_offset','TMCO2_LND_offset','TMCO2_OCN_offset','TMCO2_FFFLNDOCN_offset','TMCO2_offset'], \
                       ['SFCO2_FFF_cumulative','SFCO2_LND_cumulative','SFCO2_OCN_cumulative','SFCO2_FFFLNDOCN_cumulative','SFCO2_cumulative'], \
                       ['TMCO2_FFF_offset_minus_SFCO2_FFF_cumulative','TMCO2_LND_offset_minus_SFCO2_LND_cumulative','TMCO2_OCN_offset_minus_SFCO2_OCN_cumulative','TMCO2_FFFLNDOCN_offset_minus_SFCO2_FFFLNDOCN_cumulative','TMCO2_offset_minus_SFCO2_cumulative']]

    smoothlist=[0,0,0,0,0]
    colorlist=[1,2,0,3,4]
    shiftlist=[0,0,0,0,0]
    linestylelist=[0,0,0,0,0]
#
    code='n20260125_co2_jerry_'+expidlist[0]
#
    for variablelist in variablegrouplist:

        legendlist=variablelist
        for freqtype in freqtypelist :
            loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# ADA
#----------------------------------
description='typevarcommon'

expidgrouplist=[\
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120'] * 4, \
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10.atmco2fluxzero.20260120'] * 4 , \
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10.atmco2fluxzero.20260121'] * 4 ]

for expidlist in expidgrouplist :

    refidlist=expidlist
#
    wlist=[1.,0.]
#
    variablegrouplist=[['TMCO2_FFF','TMCO2_LND','TMCO2_OCN','TMCO2']]

    smoothlist=[0,0,0,0]
    colorlist=[1,2,0,4]
    shiftlist=[0,0,0,0]
    linestylelist=[0,0,0,0]
#
    code='n20260125_co2_jerry_nosum'+expidlist[0]
#
    for variablelist in variablegrouplist:

        legendlist=variablelist
        for freqtype in freqtypelist :
            loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


# ADA
#----------------------------------
description='typevarcommon'

expidgrouplist=[\
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120'] * 11, \
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10.atmco2fluxzero.20260120'] * 11, \
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10.atmco2fluxzero.20260121'] * 11, \
                ['n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.co2_surfacefossilfuelemis_only.20260120'] * 11, \
                ['n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.co2_aircraftemis_only.20260120'] * 11, \
                ['n1850esm.ne16pg3_tn14.noresm3_0_beta10_onlyOcnFx_20260123'] * 11, \
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10.lndco2fluxviacplocn.20260127'] * 11, \
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10.lndco2fluxviacplocn.20260127bis'] * 11, \
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10.lndco2fluxonlypos.20260127'] * 11, \
                ['n1850esm.ne16pg3_tn4.noresm3_0_beta10.lndco2fluxonlyneg.20260127'] * 11, \
                ['n1850esm.ne16pg3_tn14.noresm3_0_beta03b.BLOMalbAndBrine.2025-10-30'] * 11 ]

for expidlist in expidgrouplist :

    refidlist=expidlist
#
    wlist=[1.,0.]
#
    variablegrouplist=[['TMCO2_FFF_offset','TMCO2_LND_offset','TMCO2_OCN_offset','TMCO2_FFFLNDOCN_offset','TMCO2_offset', \
                        'SFCO2_FFF_cumulative','SFCO2_LND_cumulative','SFCO2_OCN_cumulative','SFCO2_FFFLNDOCN_cumulative','SFCO2_cumulative','SFCO2_LNDxLANDFRAC_cumulative'], \
                       ['TMCO2_FFF_trend','TMCO2_LND_trend','TMCO2_OCN_trend','TMCO2_FFFLNDOCN_trend','TMCO2_trend', \
                        'SFCO2_FFF','SFCO2_LND','SFCO2_OCN','SFCO2_FFFLNDOCN','SFCO2','SFCO2_LNDxLANDFRAC']]

    smoothlist=[0,0,0,0,0,0,0,0,0,0,0]
    colorlist=[1,2,0,3,4,1,2,0,3,4,2]
    shiftlist=[0,0,0,0,0,0,0,0,0,0,0]
    linestylelist=[0,0,0,0,0,1,1,1,1,1,2]
#
    code='n20260125_co2_jerry_combined_'+expidlist[0]
#
    for variablelist in variablegrouplist:

        legendlist=variablelist
        for freqtype in freqtypelist :
            loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)



