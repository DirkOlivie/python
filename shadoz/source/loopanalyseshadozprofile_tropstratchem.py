import loopanalyseshadozprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#----------
#
    print('+++ loopanalyseshadozprofile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard',figsize=[5,7])
#
    code='n20240220_shadoz'
#
#   PROFILE OF 
#----------------------
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
    stationlist=['ascen']
#   stationlist=['hanoi','paramaribo']
#
#   simulations
    expidlist=['NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03','NHISTfrc2_f09_tn14_20191025']
    year0list=[2010,2014]
    year1list=[2010,2014]
    legendlist=['full chemistry','aerosol only']

#   observations / simulations
#   seasonlist=['DJF','MAM','JJA','SON','YEA']
    seasonlist=['DJF']
    verticalaxislist=['height']#,'pressure']
    varlist=['ozone']#,'temperature']
#
#   subroutine 
    loopanalyseshadozprofile2.loopanalyseshadozprofile2(expidlist=expidlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, stationlist=stationlist, verticalaxislist=verticalaxislist, figlayout=figlayout, code=code)

if __name__ == '__main__':
    main()
