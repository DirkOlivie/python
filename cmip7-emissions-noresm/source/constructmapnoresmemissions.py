from netCDF4 import Dataset
import numpy as np

import se2fv

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import getdatelist

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import  yearlistmonthlist2datelist

def constructmapnoresmemissions(filename, period):
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

    '''
#
    Nav=6.022e23   # Number of Avogadro
#
#   FIND OUT MOLECULAR WEIGHT BASED ON filename
#   BC_AX, BC_N 
#   OM_NI
#   SO2, SO4_PR

    if   ( '_BC_AX_'  in filename ) : species='BC'  ; Mw=12.
    elif ( '_BC_N_'   in filename ) : species='BC'  ; Mw=12.
    elif ( '_OM_NI_'  in filename ) : species='OM'  ; Mw=12.
    elif ( '_SO2_'    in filename ) : species='SO2' ; Mw=64.
    elif ( '_SO4_PR_' in filename ) : species='SO4' ; Mw=96.
    elif ( '_S_'      in filename ) : species='S'   ; Mw=32.
    else :
        print('+++ constructseriesnoresmemissions +++')
        print('No species recognized in filename : ', filename)
        quit()
#
#   1) split period   
    line=period.split('-')
    year0=int(line[0])      # conversion string -> integer
    year1=int(line[1])      # conversion string -> integer 
    season=line[2]
#
#   list of corresponding desired dates
    datelist_desired = getdatelist.getdatelist(year0=year0,year1=year1,season=season)

        
#   2) open NetCDF file
    print(filename)
    nc_fid = Dataset(filename, 'r')

#   DIMENSIONS
#   obtain list of dimensions
    dimlist=nc_fid.dimensions.keys()

#   geographical
    if ( 'ncol' in dimlist ) : gridtype = 'irregular' ; spacerefdim='ncol' ; ncol=nc_fid.dimensions['ncol'].size                                      ; ndim_space=1
    else                     : gridtype = 'latlon'    ; spacerefdim='lat'  ; nlat=nc_fid.dimensions['lat'].size  ; nlon=nc_fid.dimensions['lon'].size ; ndim_space=2

#   time
    if ( 'time' in dimlist) :                       timerefdim='time' ; ntime=nc_fid.dimensions['time'].size ; ndim_time=1
    else :
        print('+++ constructseriesnoresmemissions +++')
        print('No time dimension recognized')
        quit()  

#   levels
    if ( 'altitude' in dimlist ) :                  levrefdim='altitude' ;  nlev=nc_fid.dimensions['altitude'].size ; ndim_lev=1
    else                         :                                                                                    ndim_lev=0 

#   BASE VARIABLES  
#   obtain latitude / longitude / area
    latitude   = np.array(nc_fid.variables['lat'][:])  # latitudes
    longitude  = np.array(nc_fid.variables['lon'][:])  # longitudes
    area       = np.array(nc_fid.variables['area'][:]) # area
    area_units =          nc_fid.variables['area'].units # area_units
    datelist   = np.array(nc_fid.variables['date'][:])   # date YYYYMMDD
#   ntime=len(datelist)

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
#   DERIVE YEAR AND MONTH LIST starting from YYYYMMDD
    yearlist  = np.zeros(ntime, dtype=int)
    monthlist = np.zeros(ntime, dtype=int)
    timelist  = np.zeros(ntime, dtype=float) 

    for itime in range(ntime) :
        yearlist[itime] = datelist[itime] / 10000
        monthlist[itime] = ( datelist[itime] % 10000 ) // 100
        timelist[ itime] = float(yearlist[itime]) + ( float(monthlist[itime]) - 0.5 ) / 12.

#   available dates    
    datelist_available = yearlistmonthlist2datelist.yearlistmonthlist2datelist(yearlist=yearlist, monthlist=monthlist)



#   DESIRED DIMENSIONS
    ndim_desired = ndim_space + ndim_lev + ndim_time
    print('Desired # dimensions in variable : ', ndim_desired)

#   SELECT CORRECT DATES
    subset = []
    for date in datelist_desired :
        index = datelist_available.tolist().index(date)  # first conversion from numpy array to list (index method only works on lists)
        subset.append(index)

#   ALL VARIABLES
    varlist = nc_fid.variables.keys()

    datalist=[]

#   loop over all variables
    for var in varlist :
        varid = nc_fid.variables[var]
        dimlist=varid.dimensions

#       check wether dimensions are ok        
        if ( len(dimlist) == ndim_desired ) : 
            field = np.array(nc_fid.variables[var][:])   # read the whole timeseries
            units =          nc_fid.variables[var].units
#
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

                if   ( gridtype == 'latlon'    ) : meanfield = np.mean(field[subset,:,:],axis=0)  # subsetting + averaging 
                elif ( gridtype == 'irregular' ) : meanfield = np.mean(field[subset,:  ],axis=0)
                else : quit()

#           3d emissions                
            elif ( ndim_lev == 1 ) :
#
#               convert units of field
                if ( units == 'molecules cm-3 s-1' ) :
                    field = field / Nav * Mw * 1.e-3 * 86400. * 365. *1.e6 # molecules -> moles > gr > kg ; sec-1 -> year-1 ; cm-3 -> m-3
                    units = 'kg m-3 yr-1'
                else :
                    print('+++ constructseriesnoresmemissions +++')
                    print('No units recognized : ', 'X'+units+'X')
                    quit()

                if   ( gridtype == 'latlon'    ) : meanfield3d = np.mean(field[subset,:,:,:], axis=0)
                elif ( gridtype == 'irregular' ) : meanfield3d = np.mean(field[subset,:,:  ], axis=0)
                else : quit()

#               sum up to column
                if   ( gridtype == 'latlon' ) :
                    meanfield = meanfield3d[0,:,:] * 0.
                    for ilev in range(nlev) :
                        meanfield[:,:] = meanfield[:,:] +  meanfield3d[ilev,:,:] * np.abs( altitude_int[ilev+1] - altitude_int[ilev] )                            
                elif ( gridtype == 'irregular' ) :
                    meanfield = meanfield3d[0,:] * 0.
                    for ilev in range(nlev) :
                        meanfield[:] = meanfield[:] +  meanfield3d[ilev,:] * np.abs( altitude_int[ilev+1] - altitude_int[ilev] )                            
                else :
                    quit()
                
            else : 
                print('+++ constructseriesnoresmemissions +++')
                print('No suitable ndim_lev recognized : ', ndim_lev)
                quit()
#
#           create data structure                
            data = { 'species'    : var+'_'+species, \
#
                     'field'      : meanfield, \
                     'longitude'  : longitude, \
                     'latitude'   : latitude, \
                     'area'       : area, \
                     'dim'        : '2d', \
                     'units'      : units, \
                     'area_units' : area_units, \
                     'period'     : period}
#
            print('before regridding ', var, species, np.sum(data['field']*data['area']) * 1.e-9, 'Tg/yr')


            if ( gridtype == 'irregular' ) :
                data = se2fv.se2fv(D=data)
                print('after regridding ', var, species, np.sum(data['field']*data['area']) *1.e-9, 'Tg/yr')
                

#           append it to the other variables
            datalist.append(data)    
#       
    nc_fid.close
#
    return datalist
