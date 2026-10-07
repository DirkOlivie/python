from netCDF4 import Dataset
import numpy as np

import filename2speciesactivity

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import fillstatistics

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-emissions-input4mips-to-noresm/source')
import getspeciesinfo


def constructseriesnoresmemissions(filename, freqtype):
#---------------------------------
    '''
    AIM
        caluculated timeseries of global totals of processed emissions
        convert units : molecules cm-2 s-1 and molecules cm-3 s-1 to Tg yr-1

    INPUT
        filename
        freqtype : 'YEA' | ...

    RETURN
        list of datastructures

    MODIFICATIONS
        (2026-04-03) : added H2
        (2026-08-26) : added S
        (2026-10-07) : introduced 

    '''
#
    Nav=6.022e23   # Number of Avogadro
#
#   FIND OUT MOLECULAR WEIGHT BASED ON filename
#   BC_AX, BC_N 
#   OM_NI
#   SO2, SO4_PR

#   COMMENTED OUT 2026-10-07
#    if   ( '_BC_AX_'  in filename ) : species='BC'  ; Mw=12.
#    elif ( '_BC_N_'   in filename ) : species='BC'  ; Mw=12.
#    elif ( '_OM_NI_'  in filename ) : species='OM'  ; Mw=12.
#    elif ( '_SO2_'    in filename ) : species='SO2' ; Mw=64.
#    elif ( '_SO4_PR_' in filename ) : species='SO4' ; Mw=96.
#    elif ( '_H2_'     in filename ) : species='H2'  ; Mw=2.
#    elif ( '_S_'      in filename ) : species='S'   ; Mw=32.
#    else :
#        print('+++ constructseriesnoresmemissions +++')
#        print('No species recognized : ', filename)
#        quit()

#   derive species and activity from filename
    species, activity = filename2speciesactivity.filename2speciesactivity(filename)

#   obtain M2
    speciesinfo = getspeciesinfo.getspeciesinfo(species=species, activity=activity)
    Mw = speciesinfo['Mw']
        
#   open NetCDF file
    print(filename)
    nc_fid = Dataset(filename, 'r')

#   DIMENSIONS
#   obtain list of dimensions
    dimlist=nc_fid.dimensions.keys()

#   geographical
    if ( 'ncol' in dimlist ) : grid = 'irregular' ; ncol=nc_fid.dimensions['ncol'].size                                      ; ndim_space=1
    else                     : grid = 'latlon'    ; nlat=nc_fid.dimensions['lat'].size  ; nlon=nc_fid.dimensions['lon'].size ; ndim_space=2

#   time
    if ( 'time' in dimlist) :                       timerefdim='time' ; ntime=nc_fid.dimensions['time'].size ; ndim_time=1
    else :
        print('+++ constructseriesnoresmemissions +++')
        print('No time dimension recognized')
        quit()  

#   levels
    if ( 'altitude' in dimlist ) :                  levrefdim='altitude' ;  nlev=nc_fid.dimensions['altitude'].size ; ndim_lev=1
    else                         :                                                                                    ndim_lev=0 

#
#   LIST OF ALL VARIABLES
    varlist = nc_fid.variables.keys()


#   BASE VARIABLES  
#   obtain latitude / longitude / area
    latitude   = np.array(nc_fid.variables['lat'][:])  # latitudes
    longitude  = np.array(nc_fid.variables['lon'][:])  # longitudesa
    datelist   = np.array(nc_fid.variables['date'][:])   # date

#   AREA (not in odl files)
    if ( 'area' in varlist) : 
        area       = np.array(nc_fid.variables['area'][:]) # area
        area_units =          nc_fid.variables['area'].units # area_units
    else :
        if ( grid == 'latlon' ) :
            area = areafraction.areafraction(longitude=longitude,latitude=latitude,outputtype='area')
            area_units='m2'
        else :
            print('+++ constructseriesnoresmemissions +++')
            print('Not possible to calculate area')
            quit()


#   ALTITUDE
    if ( 'altitude' in dimlist ) :
        altitude       = np.array(nc_fid.variables['altitude'][:])
        altitude_int   = np.array(nc_fid.variables['altitude_int'][:])
        altitude_units =          nc_fid.variables['altitude_int'].units

#       conversion altitude units : km -> m        
        if ( altitude_units == 'km' ) :
            altitude     = altitude * 1000.
            altitude_int = altitude_int * 1000.
            altitude_units = 'm'
        else :
            print('+++ constructseriesnoresmemissions +++')
            print('No altitude units recognized : ')
            quit()

#   AREA
    if ( area_units == 'm2' ) :
        print('Total area [m2] : ', np.sum(area))
        print('Should be : 509904363781790.75 m2')
    else :
        print('+++ constructseriesnoresmemissions +++')
        print('No units recognized')
        quit()

#
#   DERIVE YEAR AND MONTH LIST
    yearlist  = np.zeros(ntime, dtype=int)
    monthlist = np.zeros(ntime, dtype=int)
    timelist  = np.zeros(ntime, dtype=float) 

    for itime in range(ntime) :
        yearlist[itime] = datelist[itime] / 10000
        monthlist[itime] = ( datelist[itime] % 10000 ) // 100
        timelist[ itime] = float(yearlist[itime]) + ( float(monthlist[itime]) - 0.5 ) / 12.




#   DESIRED DIMENSIONS
    ndim_desired = ndim_space + ndim_lev + ndim_time
    print('Desired # dimensions in variable : ', ndim_desired)

#   ALL VARIABLES
    varlist = nc_fid.variables.keys()



    datalist=[]
    proflist=[]

#   loop over all variables
    for var in varlist :
        varid = nc_fid.variables[var]
        dimlist=varid.dimensions
        
        if ( len(dimlist) == ndim_desired ) : 
            field = np.array(nc_fid.variables[var][:])
            units =          nc_fid.variables[var].units
            print('units : ', units)
            print(var, 'Max - min field : ', np.max(field), np.min(field), units)
#
#            for itime in range(ntime) :
#                print(var, itime, np.max(field[itime,:,:]), np.min(field[itime,:,:]), np.mean(field[itime,:,:]), units)
#                if ( itime == 600 ) : 
#                    for ilat in range(96) :
#                        for ilon in range(144) : 
#                            print(field[itime,ilat,ilon])
#                    quit()    


#           surface emisssions    
            if ( ndim_lev == 0 ) :
#
#               convert units of field
                if ( units == 'molecules cm-2 s-1' ) : 
                    field = field / Nav * Mw * 1.e-3 * 86400. * 365. * 10000.  # molecules -> moles > gr > kg ; sec-1 -> year-1 ; cm-2 -> m-2
                    units = 'kg m-2 yr-1'
                else :
                    print('+++ constructseriesnoresmemissions +++')
                    print('No units recognized : ', units)
                    quit()                            

                valuelist=np.zeros(ntime, dtype=float) 
                for itime in range(ntime) : 
                    if ( grid == 'latlon'      ) : valuelist[itime] = np.sum(field[itime,:,:]*area[:,:]) 
                    elif ( grid == 'irregular' ) : valuelist[itime] = np.sum(field[itime,:  ]*area[:  ])
                    else : quit()

#           3d emissions                
            elif ( ndim_lev == 1 ) :
#
                print('HHEERREE')
#
#               convert units of field
                if ( units == 'molecules cm-3 s-1' ) :
                    print('AABBAABB')        

                    field = field / Nav * Mw * 1.e-3 * 86400. * 365. *1.e6 # molecules -> moles > gr > kg ; sec-1 -> year-1 ; cm-3 -> m-3
                    units = 'kg m-3 yr-1'
                    print('units (HALO): ', units)

                else :
                    print('+++ constructseriesnoresmemissions +++')
                    print('No units recognized : ', 'X'+units+'X')
                    quit()

                print('units : ', units)

                valuelist3d=np.zeros((ntime,nlev), dtype=float)
                for itime in range(ntime) :                  
                    for ilev in range(nlev) :                  
                        if   ( grid == 'latlon'    ) : valuelist3d[itime,ilev] = np.sum(field[itime,ilev,:,:]*area[:,:])
                        elif ( grid == 'irregular' ) : valuelist3d[itime,ilev] = np.sum(field[itime,ilev,:  ]*area[:  ])
                        else : quit()

#               sum up to column
                valuelist=np.zeros((ntime), dtype=float)
                for ilev in range(nlev) :
                    valuelist[:] = valuelist[:] +  valuelist3d[:,ilev] * np.abs( altitude_int[ilev+1] - altitude_int[ilev] )                            
    
#               average over time -> mean profile
                profile=np.zeros((nlev), dtype=float)
                profile[:] = np.mean(valuelist3d[:,:], axis=0)

            else : 
                print('+++ constructseriesnoresmemissions +++')
                print('No suitable ndim_lev recognized : ', ndim_lev)
                quit()
#
#           GLOBAL TOTALS
#           kg yr-1 -> Tg yr-1
            valuelist=valuelist*1.e-9
            globunits = 'Tg yr-1'

#           data structure for single variable            
            data = { 'expid'     : filename, \
                     'variable'  : var, \
                     'units'     : globunits, \
                     'fileorigin': '', \
                     'area'      : np.sum(area)    , \
                     'areaglob'  : np.sum(area), \
                     'areaunits' : 'm2', \
                     'yearlist'  : yearlist, \
                     'monthlist' : monthlist, \
                     'timelist'  : timelist, \
                     'valuelist' : valuelist, \
                     'ntime'     : ntime \
                    }

#           make monthly averages for single variable
            data = fillstatistics.fillstatistics(data=data, freqtype=freqtype)

#           append it to the other variables
            datalist.append(data)    
#       
#           PROFILE
            if ( ndim_lev == 0 ) :
                dataprofile = None
            elif ( ndim_lev == 1 ) : 
                print('units : ', units)

                dataprofile = { 'expid'     : filename, \
                                'variable'  : var, \
                                'units'     : units, \
                                'fileorigin': '', \
                                'area'      : np.sum(area)    , \
                                'areaglob'  : np.sum(area), \
                                'areaunits' : 'm2', \
                                'valuelist' : profile, \
                                'altitude'  : altitude, \
                                'altitude_int' : altitude_int, \
                                'altitude_units' : altitude_units \
                              } 
            else :
                print('+++ constructseriesnoresmemissions +++')
                print('No suitable ndim_lev recognized : ', ndim_lev)
                quit()

            proflist.append(dataprofile)           

    nc_fid.close
#
    return datalist, proflist
