import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import readattributenc
import year0year1_to_yearlistmonthlist

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-emissions-input4mips-to-noresm/source')
import getspeciesinfo


def readgfdlfield(activity, sector, species, year0, year1, scenario, i4mpdownload):
#----------------
    '''
    INPUT
        activity
        sector
        species
        year0
        year1
        scenario
        i4mpdownload

    MODIFICATIONS
        (2026-03-15) replaced 'ALL' by 'SINGLE'

    '''

#   only for H2
    if ( species != 'H2' ) :
        print('+++ readfieldh2gfdl +++')
        print('No species recognized : ', species)
        quit()

    if ( sector != 'SINGLE' ) :
        print('+++ readfieldh2gfdl +++')
        print('No sector available except SINGLE : ', sector)
        quit()

#   obtain Molar weight
    speciesinfo = getspeciesinfo.getspeciesinfo(species, activity)
    Mw = speciesinfo['Mw']    

#   Nav
    Nav=6.022e23

#   directory + filename
    dir='/scratch/olivie/code/python/cmip6-emissions-gfdl/input'
    filename=dir+'/emissions.h2.0.5x0.5.1849-2019.nc'
    year0_file=1849
    year1_file=2019
    yearlist, monthlist = year0year1_to_yearlistmonthlist.year0year1_to_yearlistmonthlist(year0=year0_file, year1=year1_file)

#   read time
    timelist_file=readnc.readnc('time', filename)    
    if ( len(yearlist) != len(timelist_file) ) : 
        print('+++ readfielh2gfdl +++')
        print('Size of time dimension differs between : ')
        print(len(yearlist))
        print(len(timelist_file))    
        quit()

#   read field
    field=readnc.readnc(activity, filename)
    units=readattributenc.readattributenc(activity, filename, 'units') # units

#   change units : molec/cm2/s -> kg m-2 s-1
    if ( units == 'molec/cm2/s' ) : 
        field = field / Nav * Mw*1.e-3 *10000.
        units = 'kg m-2 s-1'
    else :
        print('+++ readgfdlfield +++')     
        print('No units recognized')
        quit()

#   read latitude
    latitude=readnc.readnc('lat', filename)    
#   read longitude
    longitude=readnc.readnc('lon', filename)

#   calculate area [m2]
    area = areafraction.areafraction(latitude=latitude, longitude=longitude, outputtype='area')

#   subselection
    isubset = ( yearlist >= year0 ) * ( yearlist <= year1 )
#   
#    print('isubset : ', isubset)
#    print('isubset : ', sum(isubset))
#    print('year0   : ', year0)
#    print('year1   : ', year1)

#   select years one needs
    data = { 'activity'   : activity, \
             'sector'     : sector, \
             'species'    : species, \
#
             'field'      : field[isubset,:,:], \
             'longitude'  : longitude, \
             'latitude'   : latitude, \
             'area'       : area, \
             'dim'        : '2d', \
             'units'      : units, \
             'area_units' : 'm-2', \
             'yearlist'   : yearlist[isubset], \
             'monthlist'  : monthlist[isubset], \
             'ntime'      : len(yearlist[isubset])}
#
    return data

