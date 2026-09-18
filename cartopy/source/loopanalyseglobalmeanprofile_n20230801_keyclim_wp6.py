import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard',colorscheme='keyclim-wp6')
#
    generalcode='n20230801_keyclim-wp6'
#
#   CMIP6 - 20010-2014 O3
#------------------------
    expidlist=[ \
               'histssp585', \
               'histssp585-cloud2', \
               'histssp585-eddy', \
               'histssp585-iceSheet3', \
               'histssp585-ozone', \
               'histssp585-snow', \
               'histssp585-piAerOxid']
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2000,2000,2000,2000,2000,2000,2000]
    year1list=[2000,2000,2000,2000,2000,2000,2000]
#   year1list=[2014,2014,2014,2014,2014,2014,2014]
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA','YEA']
    legendlist=['Reference', \
                'Cloud', \
                'Eddy', \
                'IceSheet', \
                'Ozone', \
                'Snow', \
                'piAerOxid']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='varcommon'
    code=generalcode
#
    varlist=['mmr_OM','mmr_SULFATE','mmr_DUST','mmr_SALT','mmr_BC']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayout=figlayout, description=description, code=code)

if __name__ == '__main__':
    main()
