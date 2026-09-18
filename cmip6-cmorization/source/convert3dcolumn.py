import sys
sys.path.insert(0,'/nird/home/olivie/script-python/columnintegration')
import columnintegration

def convert3dcolumn( data, ptropdata, tdata, var ) :
#--------------------------------------------
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

        ptropdata : structure contains 
            'field'     : the data
            'longitude' : list of longitudes
            'latitude'  : list of latitues
            'nlon'      : 
            'nlat'      : nlat
            'units'     : units

        tdata : same structure as data ... (but for temperature)

        var : the variable it should become (e.g., tropoz "tropospheric ozone column")
        

    OUTPUT 
        data : structure contains
                'field'     : field, \
                'longitude' : lons, \
                'latitude'  : lats, \
                'nlon'      : nlon, \
                'nlat'      : nlat, \
                'units'     : units
    '''

    print('+++ convert3dcolumn  +++')    

    if (   var == 'tropoz' ) : varorig = 'O3' ; limit='belowtropopause'
    elif ( var == 'stratoz') : varorig = 'O3' ; limit='abovetropopause'
    else :
        print('No var recognized : ', var)
        quit()

    newfield, newunits = columnintegration.columnintegration(var=varorig, field=data['field'], unit=data['units'], hyai=data['hyai'], hybi=data['hybi'], p0= data['p0'], ps = data['ps'], ta = tdata['field'], hyam=data['hyam'], hybm=data['hybm'], limit=limit, ptrop=ptropdata['field'])

    newdata = { 'field'     : newfield, \
                'longitude' : data['longitude'], \
                'latitude'  : data['latitude'], \
                'nlon'      : data['nlon'], \
                'nlat'      : data['nlat'], \
                'units'     : newunits}
#
    print('--- convert3dcolumn ---')
#
    return newdata
