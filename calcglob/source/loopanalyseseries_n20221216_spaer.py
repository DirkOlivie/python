import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description=''


# spAero

# 1. piClim : basic comparison [absolute values]
#-----------------------------
expidlist=['NF1850norbc_f19_20190727len30', \
           'NF1850norbc_aer2014_f19_20190727', \
           'piClim-SpAer2014', \
           'piClim-SpAer2014']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['piClim-control','piClim-aer','piClim-spAero-aer','piClim-spAero-aer (enh.)']
smoothlist=[0,0,0,0]       
shiftlist=[0,0,0,0]
variablelist=['CDNUMC','CDNUMC','CDNUMC','CDNUMCmulXCDNC_SP']
code='n20221216_spaer_30yr'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
#for freqtype in freqtypelist : 
#    for typevar in typevarlist : 
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)

# 2. piClim : more simulations [absolute values]
#-----------------------------
expidlist=['NF1850norbc_f19_20190727len30', \
           'NF1850norbc_aer2014_f19_20190727', \
           'NF1850norbc_f19_20191025len30', \
           'NF1850norbc_aer2014_f19_20191025', \
           'NF1850frc2norbc_f09_20200108', \
           'NF1850frc2norbc_aer2014_f09_20200108', \
           'piClim-SpAer2014', \
           'NF1850norbc_spAer_aer2014_f19_20210523len30', \
           'piClim-SpAer2014', \
           'NF1850norbc_spAer_aer2014_f19_20210523len30']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['piClim-control','piClim-aer','piClim-control','piClim-aer','piClim-control','piClim-aer','piClim-spAero-aer','piClim-spAero-aer','piClim-spAero-aer (enh.)','piClim-spAero-aer (enh.)']
smoothlist=[0,0,0,0,0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0,0,0,0,0]
variablelist=['CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMCmulXCDNC_SP','CDNUMCmulXCDNC_SP']
code='n20221216_spaer_30yr_extended'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)

# 3. piClim : more simulations [differences]
#-----------------------------
expidlist=['NF1850norbc_aer2014_f19_20190727', \
           'NF1850norbc_aer2014_f19_20191025', \
           'NF1850frc2norbc_aer2014_f09_20200108', \
           'piClim-SpAer2014', \
           'NF1850norbc_spAer_aer2014_f19_20210523len30',
           'piClim-SpAer2014',\
           'NF1850norbc_spAer_aer2014_f19_20210523len30']        
refidlist=['NF1850norbc_f19_20190727len30', \
           'NF1850norbc_f19_20191025len30', \
           'NF1850frc2norbc_f09_20200108', \
           'NF1850norbc_f19_20190727len30', \
           'NF1850norbc_f19_20191025len30', \
           'NF1850norbc_f19_20190727len30', \
           'NF1850norbc_f19_20191025len30']
wlist=[1.,-1.]
legendlist=['piClim-aer','piClim-aer','piClim-aer','piClim-spAero-aer','piClim-spAero-aer','piClim-spAero-aer (enh.)','piClim-spAero-aer (enh.)']
smoothlist=[0,0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0,0]
variablelist=['CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMCmulXCDNC_SP','CDNUMCmulXCDNC_SP']
code='n20221216_spaer_30yr_extended_diff'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
#for freqtype in freqtypelist :
#    for typevar in typevarlist :
#        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)

# 4. historical reference : fully coupled versus fSST (no SPAERO YET)
#------------------------
expidlist=['N1850_f19_tn14_20190621len165', \
           'NHIST_f19_tn14_20190625ext', \
           'NHIST_02_f19_tn14_20190801ext', \
           'NHIST_03_f19_tn14_20190801ext', \
           'NF1850norbc_f19_20191025len165', \
           'NFHISTnorpibc_f19_20191208', \
           'NFHISTnorpibc_02_f19_20200118', \
           'NFHISTnorpibc_03_f19_20200118']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['piControl','historical','historical','historical','piClim-control','piClim-histall','piClim-histall','piClim-histall']
smoothlist=[0,0,0,0,0,0,0,0]
shiftlist=[1850-1600,0,0,0,1850-1,0,0,0]
variablelist=['CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMC']
code='n20221216_spaer_historical_cpl_versus_fsst'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)

# 5. historical : fully coupled (standard and SPAERO)
#------------------------------
# 5.1 CDNUMC
expidlist=['N1850_f19_tn14_20190621len165', \
           'NHIST_f19_tn14_20190625ext', \
           'NHIST_02_f19_tn14_20190801ext', \
           'NHIST_03_f19_tn14_20190801ext', \
           'NHIST_spAer_f19_tn14_20190925', \
           'NHIST_spAer_f19_tn14_20210523', \
           'NHIST_spAer_f19_tn14_20190925', \
           'NHIST_spAer_f19_tn14_20210523']

refidlist=expidlist
wlist=[1.,0.]
legendlist=['piControl','historical','historical','historical','hist-spAero','hist-spAero','hist-spAero (enh.)','hist-spAero (enh.)']
smoothlist=[0,0,0,0,0,0,0,0]
shiftlist=[1850-1600,0,0,0,0,0,0,0]
variablelist=['CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMCmulXCDNC_SP','CDNUMCmulXCDNC_SP']
code='n20221216_spaer_historical_cpl'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)

# 5.2 TREFHT, FSLNT, FSNT, FLNT, SWCF
expidlist=['N1850_f19_tn14_20190621len165', \
           'NHIST_f19_tn14_20190625ext', \
           'NHIST_02_f19_tn14_20190801ext', \
           'NHIST_03_f19_tn14_20190801ext', \
           'NHIST_spAer_f19_tn14_20190925', \
           'NHIST_spAer_f19_tn14_20210523']

refidlist=expidlist
wlist=[1.,0.]
legendlist=['piControl','historical','historical','historical','hist-spAero','hist-spAero']
smoothlist=[5,5,5,5,5,5]
shiftlist=[1850-1600,0,0,0,0,0]
variablelist=['FSLNT','FSNT','FLNT','TREFHT','SWCF']
code='n20221216_spaer_historical_cpl'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='varcommon',code=code,figlayout=figlayout)


# 6. historical : fixed SST + aerosol-only (standard and SPAERO)
#--------------------------
# 6.1 CDNUMC
expidlist=['NF1850norbc_f19_20191025len165', \
           'NFHISTnorpibc_aeronly_f19_20200204', \
           'NFHISTnorpibc_aeronly_02_f19_20200204', \
           'NFHISTnorpibc_aeronly_03_f19_20200204', \
           'NFHISTnorpibc_spAer_aeronly_f19_20210523', \
           'NFHISTnorpibc_spAer_aeronly_f19_20210523']

refidlist=expidlist
wlist=[1.,0.]
legendlist=['piClim-control','histSST-aer','histSST-aer','histSST-aer','histSST-spAer-aer','histSST-spAer-aer (enh.)']
smoothlist=[0,0,0,0,0,0]
shiftlist=[1850-1,0,0,0,0,0]
variablelist=['CDNUMC','CDNUMC','CDNUMC','CDNUMC','CDNUMCmulXCDNC_SP','CDNUMCmulXCDNC_SP']
code='n20221216_spaer_historical_fsst_aeronly'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description=description,code=code,figlayout=figlayout)
#        
# 6.2 FSLNT, FLNT, FSNT
expidlist=['NFHISTnorpibc_aeronly_f19_20200204', \
           'NFHISTnorpibc_aeronly_02_f19_20200204', \
           'NFHISTnorpibc_aeronly_03_f19_20200204', \
           'NFHISTnorpibc_spAer_aeronly_f19_20210523']
refidlist=['NF1850norbc_f19_20191025len165', \
           'NF1850norbc_f19_20191025len165', \
           'NF1850norbc_f19_20191025len165', \
           'NF1850norbc_f19_20191025len165']
wlist=[1.,-1.]
legendlist=['histSST-aer','histSST-aer','histSST-aer','histSST-spAer-aer']
smoothlist=[0,0,0,0]
shiftlist=[0,0,0,0]
variablelist=['FSLNT','FSNT','FLNT']
code='n20221216_spaer_historical_fsst_aeronly'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='varcommon',code=code,figlayout=figlayout, dorefaverage=1)
#
# 6. historical (SPAERO) : historical + fixe-SST aerosol-only
#--------------------------

# 6.3 FSNT_SP2_minus_FSNT_SP, FSNS_SP3_minus_FSNS_SP2, FSNT_SP3_minus_FSNT_SP
expidlist=['NHIST_spAer_f19_tn14_20190925', \
           'NHIST_spAer_f19_tn14_20210523', \
           'NFHISTnorpibc_spAer_aeronly_f19_20210523', \
           'NHIST_spAer_f19_tn14_20190925', \
           'NHIST_spAer_f19_tn14_20210523', \
           'NFHISTnorpibc_spAer_aeronly_f19_20210523', \
           'NHIST_spAer_f19_tn14_20190925', \
           'NHIST_spAer_f19_tn14_20210523', \
           'NFHISTnorpibc_spAer_aeronly_f19_20210523']
refidlist=expidlist
wlist=[1.,0.]
legendlist=['direct (hist-spAero)','direct (hist-spAero)','direct (piClim-spAeros-histaer)', \
            'cloud (hist-spAero)','cloud (hist-spAero)','cloud (piClim-spAeros-histaer)', \
            'total (hist-spAero)','total (hist-spAero)','total (piClim-spAeros-histaer)']
smoothlist=[0,0,0,0,0,0,0,0,0]
shiftlist=[0,0,0,0,0,0,0,0,0]
variablelist=['FSNT_SP2_minus_FSNT_SP' ,'FSNT_SP2_minus_FSNT_SP' ,'FSNT_SP2_minus_FSNT_SP' , \
              'FSNS_SP3_minus_FSNS_SP2','FSNS_SP3_minus_FSNS_SP2','FSNS_SP3_minus_FSNS_SP2', \
              'FSNT_SP3_minus_FSNT_SP' ,'FSNT_SP3_minus_FSNT_SP' ,'FSNT_SP3_minus_FSNT_SP']
code='n20221216_spaer_historical_spaero'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    for typevar in typevarlist :
        loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevar=typevar,freqtype=freqtype,description='',code=code,figlayout=figlayout,dorefaverage=1)
