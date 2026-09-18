import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


#figlayout=cfiglayout.CFigLayout(xrange=[0.,130.])
#figlayout=cfiglayout.CFigLayout(xrange=[0.,1050.])
figlayout=cfiglayout.CFigLayout()


# 2. NORESM2.5 and NORESM2-MM (CMIP6) and cesm3
#------------------------------------------------------------------------
#
code='n20260423_noresm2.5_picontrol_cesm316'
#
expidlist=[ \
           'N1850frc2_f09_tn14_20191001ext'                           , \
           'N1850_f19_tn14_20190621ext'                               , \
           'n1850.ne16pg3_tn14.noresm3_0_beta12a.Run10_hyb.2026-03-28', \
           'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316'              \
          ]
#
legendlist=['NorESM2-MM (1x1)', \
            'NorESM2-LM (2x2)', \
            'b12a (2x2, #385)', \
            'CESM3 (1x1, #316)']    
#
refidlist=expidlist
#
wlist=[1.,0.]
#
smoothlist=[0,0,0,0]
#
shiftlist=[-1199,-1599,-925,-69]
#
colorlist     =   [0,1,2,3]

linestylelist =   [2,0,0,2]
#

description='typevarcommon-varcommon'
variablelist=['DF_SO2', 'minusWD_SO2','EMI_SO2_TOT_noresm2','SFDMS']
variablelist=[\
#              'SOLIN', \
              'FSDS','FSDSC', \
              'PRECC','PRECL','LHFLX', \
              'TREFHT', \
#              'QREFHT', \  # not in CESM
              'FSLNT','SWCF','LWCF','PRECT','CLDTOT','CLDLOW','CLDMED','CLDHGH', \
              'U10', \
              'TGCLDLWP','TGCLDIWP']
#              'tempocn','sssgaocn','sstgaocn','salngaocn', \
#              'cb_DMS','cb_BC','cb_OM','cb_SULFATE','cb_DUST','cb_SALT']
#             'AODVISdivDAYFOC'
typevarlist=['glob']
freqtype='YEA'
#
#
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)

# ICE
freqtype='SEP'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


freqtype='MAR'
typevarlist=['NH','SH']
variablelist=['ICEFRAC']
loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)


###########################


freqtype='YEA'
typevarlist=['glob']
description='typevarcommon'

variablegrouplist=[['cb_BC','cb_BC','cb_BC','bc_a14_columnburden'], \
                   ['cb_OM','cb_OM','cb_OM','pom_a14_soa_a12_columnburden'], \
                   ['cb_SULFATE','cb_SULFATE','cb_SULFATE','so4_a123_columnburden'], \
                   ['cb_DUST','cb_DUST','cb_DUST','dst_a123_columnburden'], \
                   ['cb_SALT','cb_SALT','cb_SALT','ncl_a123_columnburden'], \
                   ['cb_SOA_A1NA','cb_SOA_A1NA','SOA_A1NA_columnburden','soa_a12_columnburden'], \
                   ['SFDMS','SFDMS','SFDMS','OCN_FLUX_DMS'], \
                   ['AOD_VISdivDAYFOC','AOD_VISdivDAYFOC','AODVISdivDAYFOC','AODVIS'], \
                   ['EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','EMI_DUST_TOT_noresm2','SFdst_a123'], \
                   ['EMI_SALT_TOT_noresm2','EMI_SALT_TOT_noresm2','EMI_SALT_TOT_noresm2','SFncl_a123']]
for variablelist in variablegrouplist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist)
