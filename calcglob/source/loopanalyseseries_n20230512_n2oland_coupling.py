import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

# MAIN PROGRAM

description='varcommon-typevarcommon'


# stratospheric aerosol

# 1. N2O EMISSION DRIVEN
#-----------------------
expidlist=['NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test01', \
           'NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test02', \
           'NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test03', \
           'NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test04', \
           'NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test05', \
           'NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test07']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['prescribed N'+r'$_2$'+'O', \
            'land emiss. (cold start)', \
            'land emiss. (warm start)', \
            'land+ocean (30%) emiss. (warm start)', \
            'land+ocean emiss. (warm start)', \
            'land+ocean emiss. (warm+spunup start)']
#
smoothlist=[0,0,0,0,0,0]
#
colorlist=[0,1,2,3,4,5]
#            
shiftlist=[0,0,0,0,0,0]
#
variablelist=['TREFHT', \
#             'F_N2O_DENIT','F_N2O_NIT', \
              'emin2oland', \
              'F_N2O_DENITxLANDFRAC','F_N2O_NITxLANDFRAC', 'F_N2O_DENIT_NITxLANDFRAC',\
              'F_N2O_DENIT_NITxLANDFRAC_as_N2O', \
              'cb_N2O','N2O_SRF','SFN2O','SFN2O_as_N', \
              'NDEP_TO_SMINNxLANDFRAC', \
              'TAU2_N2O', \
              'cb_O3']
#
code='n20230512_n2oland_coupling'
#
figlayout=cfiglayout.CFigLayout(legendlocation='outside1.7')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist : 
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# 2. Only simulations 07
#-----------------------
expidlist=['NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test07']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['land+ocean emissions']
#
smoothlist=[0]
#
colorlist=[1]
#            
shiftlist=[0]
#
variablelist=['F_N2O_DENIT_NITxLANDFRAC','SFN2O','SFN2O_as_N']
#
code='n20230512_n2oland_coupling_test07'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)

# 3. Only simulations 01 and 07
#------------------------------
expidlist=['NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test01', \
           'NF1850norbc_n2o_land_tropstratchem_prep_f19_nt14_20230510_test07']
#
refidlist=expidlist
#
wlist=[1.,0.]
#
legendlist=['prescribed N'+r'$_2$'+'O', \
            'land+ocean emissions']
#
smoothlist=[0,0]
#
colorlist=[0,1]
#            
shiftlist=[0,0]
#
variablelist=['cb_N2O','N2O_SRF']
#
code='n20230512_n2oland_coupling_test01test07'
#
figlayout=cfiglayout.CFigLayout(legendlocation='')
#
typevarlist=['glob']
freqtypelist=['YEA']
#
for freqtype in freqtypelist :
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist)
