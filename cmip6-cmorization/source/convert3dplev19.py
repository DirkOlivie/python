import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import interp3dplev19

def convert3dplev19( data) :
#---------------------------
    '''
    MODIFICATIONS
        (2024-06-10) creation

    INPUT data : structure contains
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

    newfield=interp3dplev19.interp3dplev19(field=data['field'], ps = data['ps'], p0=data['p0'], hyam=data['hyam'], hybm=data['hybm'])

    press19=[100000., 92500., 85000., 70000., 60000., 50000., 40000., 30000., 25000., \
             20000., 15000., 10000., 7000., 5000., 3000., 2000., 1000., 500., 100.]
    nlev19=len(press19)

    newdata = { 'field'     : newfield, \
                'longitude' : data['longitude'], \
                'latitude'  : data['latitude'], \
                'plev'      : press19, \
                'nlon'      : data['nlon'], \
                'nlat'      : data['nlat'], \
                'nlev'      : nlev19, \
                'units'     : data['units']}
#
    return newdata
