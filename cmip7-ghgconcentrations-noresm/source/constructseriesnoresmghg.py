from netCDF4 import Dataset
import numpy as np
import math

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/calcglob/source')
import trimseries
import fillstatistics

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

def constructseriesnoresmghg(filename, freqtype, specieslist):
#---------------------------
    '''
    INPUT
        filename
        freqtype : 'YEA'
        specieslist

    AIM
        caluculated timeseries of global totals of processed emissions
        convert units : molecules cm-2 s-1 and molecules cm-3 s-1 to Tg yr-1

    INPUT
        filename
        freqtype : 'YEA' | ... (desired frequency output)

    RETURN
        list of datastructures

    '''
#
    Rearth = 6.370e6
    Aearth = 4. * math.pi * Rearth * Rearth


#   open NetCDF file
    print(filename)
    nc_fid = Dataset(filename, 'r')

#   1. DIMENSIONS
#   obtain list of dimensions
    dimlist=nc_fid.dimensions.keys()

#   geographical    
    if ( 'lat' in dimlist ) : 
        nlat       = nc_fid.dimensions['lat'].size
        latitude   = np.array(nc_fid.variables['lat'][:])  # latitudes
        latweight  = np.cos([latitude * math.pi / 180.])
        ndim_space = 1
    else :
        ndim_space = 0

#   datelist read from file
    if ( 'time' in dimlist) :
        ntime     = nc_fid.dimensions['time'].size
        datelist  = np.array(nc_fid.variables['date'][:])   # date
        ndim_time = 1
    else :
        print('+++ constructseriesnoresmemissions +++')
        print('No time dimension recognized')
        quit()  
#
#
#   2. TIME DERIVE YEAR AND MONTH LIST
    yearlist  = np.zeros(ntime, dtype=int)
    monthlist = np.zeros(ntime, dtype=int)
    timelist  = np.zeros(ntime, dtype=float) 

    for itime in range(ntime) :
        yearlist[itime]  = datelist[itime] / 10000
        monthlist[itime] = ( datelist[itime] % 10000 ) // 100
        timelist[ itime] = float(yearlist[itime]) + ( float(monthlist[itime]) - 0.5 ) / 12. # decimal year

#   ORIGINAL DATA MONTHLY OR ANNUAL
    if   ( set([1,2,3,4,5,6,7,8,9,10,11,12]).issubset(monthlist) ) : origfreqtype='monthly'
    elif ( ( yearlist[-1]-yearlist[0] + 1 ) == ntime ) : origfreqtype='YEA'
    else :
        print('+++ constructseriesnoresmghg +++')
        print('No origfreqtype recognized')
        quit()
    print('origfreqtyp : ', origfreqtype)

#   DESIRED DIMENSIONS
    ndim_desired = ndim_space + ndim_time
    print('Desired # dimensions in variable : ', ndim_desired)

#   ALL VARIABLES
    varlist = nc_fid.variables.keys()

    datalist=[]

#   3. loop over all variables
    for var in varlist :
        varid = nc_fid.variables[var]
        dimlist=varid.dimensions
        
        if ( ( len(dimlist) == ndim_desired ) and ( var in specieslist ) ) : 
            field = np.array(nc_fid.variables[var][:])
            units =          nc_fid.variables[var].units
            print('units : ', units)
            print(var, 'Max - min field : ', np.max(field), np.min(field), units)
#
            valuelist=np.zeros(ntime, dtype=float) 
            for itime in range(ntime) : 
                if   ( ndim_space == 0 ) : valuelist[itime] = field[itime]                                               # original data is already global mean
                elif ( ndim_space == 1 ) : valuelist[itime] = np.sum(field[itime,:]*latweight[:]) / np.sum(latweight[:]) # average over zonal
                else :
                    print('No #spatial dimensions recognized : ', ndim_space)
                    quit()

#                if (timelist[itime] >= 2000) :
#                    print(var, timelist[itime], field[itime,:])

 
#           data structure for single variable            
            data = { 'expid'     : filename, \
                     'variable'  : var, \
                     'units'     : units, \
                     'fileorigin': '', \
                     'area'      : Aearth, \
                     'areaglob'  : Aearth, \
                     'areaunits' : 'm2', \
                     'yearlist'  : yearlist, \
                     'monthlist' : monthlist, \
                     'timelist'  : timelist, \
                     'valuelist' : valuelist, \
                     'ntime'     : ntime \
                    }
#

            if ( origfreqtype == 'monthly') : 
#               trimseries to only have full years
                data = trimseries.trimseries(data=data)

#               make monthly averages for single variable
                data = fillstatistics.fillstatistics(data=data, freqtype=freqtype)

            elif ( origfreqtype == 'YEA' and freqtype == 'YEA' ) : 
#               
                print('No action needed')

            else :
                print('+++ constructseriesnoresmghg +++')    
                print('Incompatible origfreqtype and freqtype : ', origfreqtype, freqtype)
                quit()
#
#           append it to the other variables
            datalist.append(data)

    nc_fid.close
#
    return datalist
