import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
import getcoherentcolorlist
#
def main():
#-------
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout0=cfiglayout.CFigLayout(code='log',xtype='log',ytype='log') # log scale for y-axis (height or pressure)
    figlayoutlist=[figlayout0]
#
#   reflegendlist=['CESM2','EMAC','GEOS-Chem','GFDL','GISS free','GISS nudged','NorESM2-LM','UKESM']
#    reflegendlist=['EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM','CESM2','GEOS-Chem','GISS free']
#    refcolorlist=[0,1,2,3,4,5,6,7]


# Abdul-Razak Gahn / Betancourt Nenes
#----------------------------------------------------------------------------------------
    expidlist=[ \
           'N1850_f19_tn14_20190621ext', \
           'N1850_f19_tn14_20231204_test05', \
            \
#           'N1850_f19_tn14_20231204_test15', \
#           'N1850_f19_tn14_20231204_test16', \
#           'N1850_f19_tn14_20231204_test14', \
#           'N1850_f19_tn14_20231204_test17', \
            \
           'N1850_f19_tn14_20231204_test13', \
           'N1850_f19_tn14_20231204_test03', \
           'N1850_f19_tn14_20231204_test11', \
           'N1850_f19_tn14_20231204_test12', \
            \
           'N1850_f19_tn14_20241127_test01']

    legendlist=[ \
            'noresm2 (CMIP6)', \
            'noresm2.1 (no CAM corr.)', \
             \
#            'noresm2.1 (only ice-delimiter corr.)', \
#            'noresm2.1 (only het. freez. corr.)', \
#            'noresm2.1 (only koagsub corr.)', \
#            'noresm2.1 (only dry dep. corr.)', \
             \
            'noresm2.1 (no koagsub corr.)', \
            'noresm2.1 (no ice-delimiter corr.)', \
            'noresm2.1', \
            'noresm2.1 + SH/TS', \
            \
            'noresm2.3']


    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1620,1620,1620,1620,1620,1620,1620]
    year1list=[1629,1629,1629,1629,1629,1629,1629]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    colorlist=[0,1,2,3,4,5,6]
#  colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['pressure']
#
    description='varcommon'
    code='n20241201_noresm2.3_cpl'
#
#   variables
    varlist=['mmr_BC','mmr_SULFATE','mmr_DUST','mmr_SALT','mmr_OM','SOA_A1','SOA_NA']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
if __name__ == '__main__':
    main()

