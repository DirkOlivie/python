import loopanalysezonalmeanline2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#----------
#
    print('+++ loopanalysezonalmeanline +++')
#
    figlayout=cfiglayout.CFigLayout()
    figlayoutlist=[figlayout]
    horizontalaxislist=['']    
    regionlist=['glob']
#
    code='n20250520_esm2025_ch4_amip'
#
#    varlist=['CH4_SRF','O3_SRF']
#
# 1. ch4_surfacelayer [CNRM / NorESM2 / UKESM / CanESM5]
#-------------------------------------------------------
    expidlist=['CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
               'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
               'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
               'UKESM1-0-LL_amip-CH4ems_r1i1p1f2_gn', \
               'CanESM5-1c-amip-ch4p-test5_amip_r1i1p1f1_gn', \
               'MIROC-ES2L-CHEM_amip_r1i1p1f1_gn']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2010,2010,2010,2010,2010,2010]
    year1list=[2014,2014,2014,2014,2014,2014]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,0,2,0,0,0]
    colorlist=[0,1,1,2,3,4]
    legendlist=['CNRM-ESM2-1 (AMIP-ch4ems)', \
                'NorESM2.3-LM-C (AMIP-ch4ems)', \
                'NorESM2.3-LM-C (AMIP)', \
                'UKESM1-0-LL (AMIP-ch4ems)', \
                'CanESM5-1c (AMIP-ch4ems)', \
                'MIROC-ES2L-CHEM (AMIP-ch4ems)']
#
    description=''
    vargrouplist = [ \
                    ['ch4_surfacelayer','CH4_SRF','CH4_SRF','ch4_surfacelayer','ch4_surfacelayer','ch4_surfacelayer'] \
                     ]  
#
    for varlist in vargrouplist :
        loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

# 2. o3_surfacelayer [CNRM / NorESM2 / UKESM ]
#----------------------------------------------
    expidlist=['CNRM-ESM2-1_AESM-amip_r1i1p1f2_gr', \
               'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
               'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
               'UKESM1-0-LL_amip-CH4ems_r1i1p1f2_gn']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2010,2010,2010,2010]
    year1list=[2014,2014,2014,2014]
    seasonlist=['YEA','YEA','YEA','YEA']
    linestylelist=[0,0,2,0]
    colorlist=[0,1,1,2]
    legendlist=['CNRM-ESM2-1 (AMIP-ch4ems)', \
                'NorESM2.3-LM-C (AMIP-ch4ems)', \
                'NorESM2.3-LM-C (AMIP)', \
                'UKESM1-0-LL (AMIP-ch4ems)']
#
    description=''
    vargrouplist = [ \
                    ['o3_surfacelayer','O3_SRF','O3_SRF','o3_surfacelayer'] \
                     ]  
#
#    for varlist in vargrouplist :
#        loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

# 3. NorESM2
#-----------
    expidlist=['NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
               'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506', \
               'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506', \
               'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2010,2010,2010,2010]
    year1list=[2014,2014,2014,2014]
    seasonlist=['DJF','JJA','DJF','JJA']
    linestylelist=[0,2,0,2]
    colorlist=[0,0,1,1]
    legendlist=['conc-driven (DJF)','conc-driven (JJA)','emis-driven (DJF)','emis-driven (JJA)']
#
#    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

if __name__ == '__main__':
    main()
