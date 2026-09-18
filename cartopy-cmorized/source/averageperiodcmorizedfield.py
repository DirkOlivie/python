import numpy as np

import selectperiodcmorizedfield

def averageperiodcmorizedfield ( expid, var, year0, year1, season):
#-----------------------------
    '''
    MODIFICATIONS

    INPUT
        expid
        var
        year0
        year1
        season

    RETURNS
        structure containing profile data

    CALLS
        getdatelist
        getvarcomponents
        readallcmorizedfield
    '''
    print('+++ averageperiodcmorizedfield +++')
#
# get the selected data
    data=selectperiodcmorizedfield.selectperiodcmorizedfield(expid=expid, var=var, year0=year0, year1=year1, season=season)

# average all the data over the time dimensions (first axis)
    newdata = { 'field' : np.mean(data['field'],axis=0), \
                'longitude' : data['longitude'], \
                'latitude'  : data['latitude'], \
                'nlon'      : data['nlon'], \
                'nlat'      : data['nlat'], \
                'nlev'      : data['nlev'], \
                'units'     : data['units'], \
                'season'    : season, \
                'year0'     : year0, \
                'year1'     : year1}
#   in case of 4d data
    if( data['nlev'] != 0 ) :
        newdata.update({'pfull'       : np.mean(data['pfull'],axis=0), \
#                        'phalf'       : np.mean(data['phalf'],axis=0), \
                        'units_pfull' : data['units_pfull']})
#                        'units_phalf' : data['units_phalf']})       
#
    print('--- averageperiodcmorizedfield ---')
#
    return newdata
