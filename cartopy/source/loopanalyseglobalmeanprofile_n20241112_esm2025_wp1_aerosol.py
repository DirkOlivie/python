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
    figlayout0=cfiglayout.CFigLayout(code='log',xtype='log',ytype='log',colorscheme='idl') # log scale for y-axis (height or pressure)
    figlayout1=cfiglayout.CFigLayout(code=''   ,xtype='log',ytype=''   ,colorscheme='idl') # linear scale
    figlayoutlist=[figlayout0,figlayout1]
#
#   reflegendlist=['CESM2','EMAC','GEOS-Chem','GFDL','GISS free','GISS nudged','NorESM2-LM','UKESM']
#    reflegendlist=['EMAC','GFDL','GISS nudged','NorESM2-LM','UKESM','CESM2','GEOS-Chem','GISS free']
#    refcolorlist=[0,1,2,3,4,5,6,7]


# Abdul-Razak Gahn / Betancourt Nenes
#----------------------------------------------------------------------------------------
    expidlist=[\
               'nf1850norbc_aer2014.f19.f19_base2.0.9_20241025', \
               'nf1850norbc_aer2014.f19.f19_BNForces_20241025']

    refidlist=expidlist
    wlist=[1.,0.]
#    
#   year0list=[11,11]
    year0list=[26,26]
    year1list=[30,30]
    seasonlist=['YEA','YEA']
    legendlist=['Reference','BN']
    colorlist=[1,2]
#  colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20241112_esm2025_wp1_aerosolactivation'
#
#   variables
    varlist=['mmr_BC','mmr_SULFATE','mmr_DUST','mmr_SALT','mmr_OM']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
# Abdul-Razak Gahn / Betancourt Nenes
#----------------------------------------------------------------------------------------
    expidlist=[\
              'nf1850norbc_aer2014.f19.f19_base2.0.9_20241025', \
              'nf1850norbc_aer2014.f19.f19_convact1_20241104',    \
              'nf1850norbc_aer2014.f19.f19_convscavYu_20241104', \
              'nf1850norbc_aer2014.f19.f19_updraftscav_20241106', \
              'nf1850norbc_aer2014.f19.f19_noctran_20241104',     \
              'nf1850norbc_aer2014.f19.f19_fraciscldc_20241105',  \
              'nf1850norbc_aer2014.f19.f19_fracis2step_20241105']
    refidlist=expidlist
    wlist=[1.,0.]
#    
#   year0list=[11,11,11,11,11,11]
    year0list=[26,26,26,26,26,26,26]
    year1list=[30,30,30,30,30,30,30]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['Reference', \
                'cscav1', \
                'cscavYu', \
                'cscavUP', \
                'ctran0', \
                'ctranC', \
                'CtranCS']
    colorlist=[1,2,3,4,5,6,7]
#  colorlist=getcoherentcolorlist.getcoherentcolorlist(legendlist=legendlist, reflegendlist=reflegendlist, refcolorlist=refcolorlist)
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code='n20241112_esm2025_wp1_convectivescavenging'
#
#   variables
    varlist=['mmr_BC','mmr_SULFATE','mmr_DUST','mmr_SALT','mmr_OM']
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist)
#
if __name__ == '__main__':
    main()



