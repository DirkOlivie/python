import loopanalyseshadozprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#----------
#
    print('+++ loopanalyse hyway profile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard',figsize=[5,7])
#
    code='n20251001_hyway'
#
#   PROFILE OF 
#----------------------
    stationlist=['ascen']
#    expidlist=['UKESM1-0-LL_hyway_transient2010s_r1']
    expidlist=['EC-Earth3-AerChem_hyway_transient2010s_r1', \
               'UKESM1-0-LL_hyway_transient2010s_r1']
    year0list=[2010,2010]
#    year1list=[2019,2019]
    year1list=[2010,2010]
#   legendlist=['UKESM1-0-LL']
    legendlist=['EC-Earth3-AerChem', \
                'UKESM1-0-LL']   
    seasonlist=['YEA','YEA']
    verticalaxislist=['height'] # ['height']
#    verticalaxislist=['pressure']
    varlist=['ozone']
#    loopanalyseshadozprofile2.loopanalyseshadozprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, stationlist=stationlist, verticalaxislist=verticalaxislist, figlayout=figlayout, code=code)


#   observations
    stationlist=['ascen', \
                 'costarica', \
                 'fiji', \
                 'hanoi', \
                 'hilo', \
                 'irene', \
                 'java', \
                 'kuala', \
                 'nairobi', \
                 'natal', \
                 'paramaribo', \
                 'reunion', \
                 'samoa', \
                 'sancrist']
#
#    stationlist=['ascen']
#   stationlist=['hanoi','paramaribo']
#
#   simulations
    expidlist=['CESM2-v212_hyway_transient2010s_r1', \
               'EC-Earth3-AerChem_hyway_transient2010s_r1', \
               'EMAC-DLR_hyway_transient2010s_r1', \
               'LMDZ-INCA_hyway_transient2010s_r1', \
               'NorESM2-LM-C_hyway_transient2010s_r1i1p1f1', \
               'OsloCTM3v1-2_hyway_transient2010s_r1', \
               'UKESM1-0-LL_hyway_transient2010s_r1']
    year0list=[2010,2010,2010,2010,2010,2010,2010]
#   year1list=[2010,2010,2010,2010,2010,2010,2010]
    year1list=[2019,2019,2019,2019,2019,2019,2019]
    legendlist=['CESM2-v212', \
                'EC-Earth3-AerChem', \
                'EMAC-DLR', \
                'LMZ-INCA', \
                'NorESM2-LM-C', \
                'OsloCTM3v1-2', \
                'UKESM1-0-LL']

#   observations / simulations
#   seasonlist=['DJF','MAM','JJA','SON','YEA']
    seasonlist=['YEA']
#    verticalaxislist=['height']#,'pressure']
    verticalaxislist=['pressure']
    varlist=['ozone']#,'temperature']
#
#   subroutine 
    loopanalyseshadozprofile2.loopanalyseshadozprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, stationlist=stationlist, verticalaxislist=verticalaxislist, figlayout=figlayout, code=code)

if __name__ == '__main__':
    main()
