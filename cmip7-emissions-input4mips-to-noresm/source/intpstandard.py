import checkglobaltotal

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')

import getgridtype
import lon2lonbnds
import lat2latbnds
import intpfieldregular
import intpfieldirregular

sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-emissions-volc/source')
import readareatopography

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

def intpstandard(D, longitude, latitude, resolution, filelocation, altitude_int=None):
#---------------
    '''
    INPUT
        D             : structure with original latlon field
        longitude     : final/desired longitude
        latitude      : final/desired latitude
        resolution    : final/desired grid 'latlon' or 'irregular'     
        filelocation  : 
        altitude_int  : final/desired altitude_int

    CALLS
        lon2lonbnds
        lat2latbnds
        intpfieldregular
        intpfieldirregular
                
    MODIFICATIONS
        (2025-10-18) added possibility for irregular grid
        (2025-09-29) added yearlist and monthlist to output structure

    '''

#   original grid
    bdlon0=lon2lonbnds.lon2lonbnds(longitude=D['longitude'])
    bdlat0=lat2latbnds.lat2latbnds(latitude=D['latitude'])

#   final grid
    gridtype=getgridtype.getgridtype(resolution=resolution) #   0.9x1.25 -> gridtype : latlon
                                                            #   1.9x2.5  -> gridtype : latlon
                                                            #   ne30pg3  -> gridtype : irregular
                                                            #   ne16pg3  -> gridtype : irregular
#
    if ( gridtype == 'latlon' ) :
        bdlon=lon2lonbnds.lon2lonbnds(longitude=longitude)
        bdlat=lat2latbnds.lat2latbnds(latitude=latitude)
    
#   area of new grid
    if (   gridtype == 'latlon'    ) : area=areafraction.areafraction(longitude=longitude,latitude=latitude,outputtype='area')
    elif ( gridtype == 'irregular' ) : area=readareatopography.readareatopography(grid=resolution, variable='area', filelocation=filelocation)
    else :
        print('+++ intpvolcano +++')
        print('No gridtype recognized')
        quit()

#   interpolate to the new grid
#   2-dimensional
    if ( D['dim'] == '2d' ) :
#       horizontal interpolation

        if   ( gridtype == 'latlon'    ) : field1 = intpfieldregular.intpfieldregular(    infield=D['field'], latinbd=bdlat0, latoutbd=bdlat, loninbd=bdlon0, lonoutbd=bdlon)
        elif ( gridtype == 'irregular' ) : field1 = intpfieldirregular.intpfieldirregular(infield=D['field'], latin=D['latitude'], latout=latitude, lonin=D['longitude'], lonout=longitude, filelocation=filelocation)
        else : 
            print('+++ intpstandard +++')
            print('No gridtype recognized : ', gridtype)
            quit()

        data = { 'activity'  : D['activity'], \
                 'sector'    : D['sector'], \
                 'species'   : D['species'], \
#
                 'field'      : field1, \
                 'units'      : D['units'], \
#
                 'longitude'  : longitude, \
                 'latitude'   : latitude, \
                 'resolution' : resolution, \
#
                 'area'       : area, \
                 'area_units' : 'm2', \
#
                 'dim'        : D['dim'], \
#
                 'yearlist'  : D['yearlist'], \
                 'monthlist' : D['monthlist'], \
                 'ntime'      : D['ntime']}
#
#   3-dimensional
    elif ( D['dim'] == '3d' ) :

#       interpolate to final grid
        if   ( gridtype == 'latlon'    ) : field1 = intpfieldregular.intpfieldregular(infield=D['field'], latinbd=bdlat0, latoutbd=bdlat, loninbd=bdlon0, lonoutbd=bdlon, levinbd=D['altitude_int'],levoutbd=altitude_int)
        elif ( gridtype == 'irregular' ) : field1 = intpfieldirregular.intpfieldirregular(infield=D['field'], latin=D['latitude'], latout=latitude, lonin=D['longitude'], lonout=longitude, filelocation=filelocation, levinbd=D['altitude_int'], levoutbd=altitude_int)
        else :
            print('+++ intpstandard +++')
            print('No gridtype recognized : ', gridtype)
            quit()

#
        data= { 'activity'  : D['activity'], \
                'sector'    : D['sector'], \
                'species'   : D['species'], \
#
                'field'      : field1, \
                'units'      : D['units'], \
#
                'longitude'  : longitude, \
                'latitude'   : latitude, \
                'resolution' : resolution, \
#                'altitude_int'  : altitude_int, \
#                'altitude_units' : D['altitude_units'], \
                'area'       : area, \
                'area_units' : 'm2', \
#
                'levbnds'   : altitude_int, \
                'lev_units' : D['altitude_units'], \
                'dim'       : D['dim'], \
#
                'yearlist'  : D['yearlist'], \
                'monthlist' : D['monthlist'], \
                'ntime'     : D['ntime'] }     
    else :
        print('No dimension recognized = ', D['dim'])
        quit()
#
#   ADD area
#    if (   gridtype == 'latlon'    ) : area = areafraction.areafraction(longitude=longitude,latitude=latitude,outputtype='weightradians')      
#    elif ( gridtype == 'irregular' ) : area = areafractionirregular.areafractionirregular(longitude=longitude,latitude=latitude,resolution=resolution,irreggridversion=irreggridversion,outputtype='weightradians')
#    else :
#        print('No dimension recognized = ', D['dim'])
#        quit()
#
#    data.update({'area' : area, 'areaunits' : 'radians^2'})

#   SHOULDE BE ACTIVATED : but D contains altitude_int and checkglobaltotal wants lev_bnds
    globaltotal=checkglobaltotal.checkglobaltotal(D=data)

    return data
