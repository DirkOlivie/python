import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import readsingleh0field

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getstandardunits


def readmodelmonth(expid, var, year, month):
#-----------------
    '''
    INPUT
        expid
        var
        year
        month

    RETURN
        structure containing 
            var
            field
            longitude
            latitude
            mask : will be put everwyere to 1
               
    CALLED BY
       readobsmodelperiod
    '''
    cyear =str("%4.4i"% (year))
    cmonth=str("%2.2i"% (month))
    date=cyear+'-'+cmonth
#
    if ( var == 'toc' ) :
        cvar='cb_O3'
    elif ( var == 'od550aer' ) :
        cvar='DOD550'
    else : 
        print('No var recognized : ', var)
        quit()

    D = readsingleh0field.readsingleh0field(expid=expid, var=cvar, date=date) # does not contain a mask
#
    units=getstandardunits.getstandardunits(units=D['units'])
#
    data = { 'var'       : var, \
             'units'     : units, \
             'field'     : D['field'], \
             'longitude' : D['longitude'], \
             'latitude'  : D['latitude'], \
             'mask'      : D['field'] * 0. + 1.}  # field exists everywhere 

    return data
