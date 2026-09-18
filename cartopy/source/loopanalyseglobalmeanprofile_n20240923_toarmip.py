import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard')
    figlayoutlist=[figlayout]
#
# Absolue values
#----------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[31,31,31]
    year1list=[40,40,40]
    seasonlist=['YEA','YEA','YEA']
    legendlist=['O3-clim from reference', \
                'O3-clim from O3-prec. 2050', \
                'O3-clim from O3-prec+aer. 2050']
    colorlist=[0,1,2]
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20240923_toarmip'
#
#   variables
    varlist=['CLOUD']
    varlist=['CONCLD']
    varlist=['Q','RELHUM']
    varlist=['RELHUM']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)

#
# Differences
#----------------------------------------------------------------------------------------
    expidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01']               
    refidlist=['NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01', \
               'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01']
    wlist=[1.,-1.]
#    
    year0list=[31,31]
    year1list=[40,40]
    seasonlist=['YEA','YEA']
    legendlist=['O3-clim from O3-prec. 2050', \
                'O3-clim from O3-prec+aer. 2050']
    colorlist=[1,2]
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20240923_toarmip_diffabs'
#
#   variables
    varlist=['CLOUD']
    varlist=['CONCLD']
    varlist=['Q','RELHUM']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)

#

if __name__ == '__main__':
    main()
