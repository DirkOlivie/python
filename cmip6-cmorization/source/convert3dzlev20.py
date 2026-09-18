import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import interp3dzlev20

def convert3dzlev20( data, zdata) :
#---------------------------
    '''
    MODIFICATIONS
        (2024-06-10) creation

    INPUT 
        data : structure contains
            'field'     : the data
            'longitude' : list of longitudes
            'latitude'  : list of latitues
            'nlon'      : 
            'nlat'      : nlat
            'nlev'      : nlev
            'units'     : units
            'p0'        : p0
            'ps'        : ps
            'hyai'      : hyai
            'hybi'      : hybi
            'hyam'      : hyam
            'hybm'      : hybm
            'units_ps'  : units_ps
            'units_p0'  : units_p0
        zdata : structure contains [the (geopotential) height in 'm']
            ...
     
    OUTPUT data : structure contains
        'field'     : field, \
                'longitude' : lons, \
                'latitude'  : lats, \
                'plev'      : plevs, \
                'nlon'      : nlon, \
                'nlat'      : nlat, \
                'nlev'      : nlev, \
                'units'     : units
    '''

    print('+++ convert3dzlev20 +++')

    newfield=interp3dzlev20.interp3dzlev20(field=data['field'], zfield=zdata['field'], zunits=zdata['units'])

    zlev20 = [ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, \
              10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5,19.5 ]

    nlev20=len(zlev20)

    newdata = { 'field'     : newfield, \
                'longitude' : data['longitude'], \
                'latitude'  : data['latitude'], \
                'zlev'      : zlev20, \
                'nlon'      : data['nlon'], \
                'nlat'      : data['nlat'], \
                'nlev'      : nlev20, \
                'units'     : data['units']}
#
    print('--- convert3dzlev20 ---')
#
    return newdata
