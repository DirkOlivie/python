import experimentdefinition
import readmeanglobalmeanprofile_rawnoresm

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cartopy-cmorized/source')
import readmeanglobalmeanprofile_cmorizedfield

def readmeanglobalmeanprofile ( expid, var, year0, year1, season, verticalaxis, region=None, xlon=None, xlat=None):
#----------------------------
    '''
    INPUT
        expid
        var
        year0
        year1
        season
        region
        verticalaxis     

    MODIFICATIONS
        (2022-11-18) extension until components
        (2025-10-04) extension with specific xlat and xlon, and default for region

    CALLS
        readmeanglobalmeanprofile_rawnoresm
        readmeanglobalmeanprofile_cmorized
    '''
    print('+++ readmeanglobalmeanprofile +++')

    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    dataformat=expidinfo['dataformat']

    if (   dataformat == 'rawnoresm' ) : amean = readmeanglobalmeanprofile_rawnoresm.readmeanglobalmeanprofile_rawnoresm(expid=expid, var=var, year0=year0, year1=year1, season=season, region=region, xlon=xlon, xlat=xlat, verticalaxis=verticalaxis)
    elif ( dataformat == 'cmorized'  ) : amean = readmeanglobalmeanprofile_cmorizedfield.readmeanglobalmeanprofile_cmorizedfield(expid=expid, var=var, year0=year0, year1=year1, season=season, region=region, xlon=xlon, xlat=xlat, verticalaxis=verticalaxis)    
    else : 
        print('No dataformat recognized : '+dataformat)
        quit()
#
    print('--- readmeanglobalmeanprofile ---')
#
    return amean
