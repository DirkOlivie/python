from netCDF4 import Dataset
import netCDF4 as nc
import numpy as np


def readfile_cdr(var, wvlresolution):
#---------------------
    '''
    INPUT
        var        : 'SSI' (no wavelength resolution) or 'TSI' (with wavelength resolution)
        resolution : 'standard' or 'high'
   
    REMARK
        currently only annual file

    RETURN



    VARIABLES IN NETCDF FILE
    1. standard resolution
        type  | variable              | dimension          | long_name                                                                          | standard_name                          | units                            | cell_methods | auxilialiary variables | missing_value  | axis | bounds   |
        ------|-----------------------|--------------------|------------------------------------------------------------------------------------|----------------------------------------|----------------------------------|--------------|------------------------|----------------|------|----------| 
        float | SSI                   | (time, wavelength) | "NOAA Climate Data Record of Yearly Solar Spectral Irradiance (W m-2 nm-1)"        | "solar_irradiance_per_unit_wavelength" | "W m-2 nm-1"                     | "time: mean" | "SSI_UNC"              | -99.f          |      |          |
	    float | wavelength            | (wavelength)       | "Wavelength grid center"                                                           | "radiation_wavelength"                 | "nm"                             |              |                        |                |      |          |
	    float | Wavelength_Band_Width | (wavelength)       | "Wavelength band width. Centered on wavelength."                                   |                                        | "nm"                             |              |                        |                |      |          |
	    float | TSI                   | (time)             | "NOAA Climate Data Record of Yearly Total Solar Irradiance (W m-2)"                | "solar_irradiance"                     | "W m-2"                          | "time: mean" | "TSI_UNC"              | -99.f          | T    | time_bnds| 
	    float | time                  | (time)             |                                                                                    | "time"                                 | "days since 1610-01-01 00:00:00" |              |                        |                |      |          | 
	    float | TSI_UNC               | (time)             | "Uncertainty in Yearly Total Solar Irradiance (W m-2)"                             |                                        | "W m-2"                          |              |                        | -99.f          |      |          |   
	    float | time_bnds             | (time, bounds)     | "Minimum (inclusive) and maximum (exclusive) dates included in the time averaging" |                                        | "days since 1610-01-01 00:00:00" |              |                        |                |      |          | 
	    float | SSI_UNC               | (time, wavelength) | "Uncertainty in Yearly Solar Spectral Irradiance (W m-2 nm-1)"                     |                                        | "W m-2 nm-1"                     |              |                        | -99.f          |      |          | 

        There is no calendar given but works well.  Days since beginning of year is always 181 : 1st July 00h00


    2. high resolution
        type  | variable   | dimension           | long_name                                                                          | standard_name                          | units                            | cell_methods | missing_value | axis | bounds     |
        ------|------------|---------------------|------------------------------------------------------------------------------------|----------------------------------------|----------------------------------|--------------|---------------|------|------------|
	    float | SSI        | ( time, wavelength) | "NOAA Climate Data Record of Yearly Solar Spectral Irradiance (W m-2 nm-1)"        | "solar_irradiance_per_unit_wavelength" | "W m-2 nm-1"                     | "time: mean" | -99.f         |      |            |   
 	    float | wavelength | (wavelength)        | "Wavelength grid center"                                                           | "radiation_wavelength"                 | "nm"                             |              |               |      |            | 
	    float | time       | (time)              |                                                                                    | "time"                                 | "days since 1610-01-01 00:00:00" |              |               |"T"   | time_bnds" |
	    float | time_bnds  | (time, bounds)      | "Minimum (inclusive) and maximum (exclusive) dates included in the time averaging" |                                        | "days since 1610-01-01 00:00:00" |              |               |      |            |         

    '''

#   directory
    dir='/datalake/NS2345K/olivie/volcaod-auxiliary/solar-spectrum-cdr'

#   filename
    if ( wvlresolution == 'standard' ) :
        nc_f=dir+'/ssi_v03r00_yearly_s1610_e2024_c20250221.nc'
    elif ( wvlresolution == 'high' ) :
        nc_f=dir+'/hires-ssi_v03r00_yearly_s1610_e2024_c20250310.nc'
    else :
        print('+++ readspectrum_cdr +++')
        print('No resolution recognized : ', resolution)
        quit()

    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')

#   wavelength
    wavelength=np.array(nc_fid.variables['wavelength'][:])
    wavelength_units=nc_fid.variables['wavelength'].units

#   wavelength band with
    wavelength_width=np.array(nc_fid.variables['Wavelength_Band_Width'][:])
    wavelength_width_units=nc_fid.variables['Wavelength_Band_Width'].units

#   time
    time=np.array(nc_fid.variables['time'][:])
    time_units=nc_fid.variables['time'].units
#   time_calendar=nc_fid.variables['time'].calendar # no calendar given

#   field
    field=np.array(nc_fid.variables[var][:]) # read the actual field
    units=nc_fid.variables[var].units

    print(nc_fid.variables[var].dimensions)

    nc_fid.close
#
#   DATE TIME
    ntime=len(time)

    yearlist=np.zeros(ntime, dtype=int)
    monthlist=np.zeros(ntime, dtype=int)
    decimalyearlist=np.zeros(ntime, dtype=float)

    datetime=[]
    for itime in range(ntime) :
        tmp=nc.num2date(time[itime], time_units)
        datetime.append(tmp)

        yearlist[itime]=tmp.year
        monthlist[itime]=tmp.month
        decimalyearlist[itime]=float(tmp.year) + ( float(tmp.month)-0.5 ) / 12.


        if ( itime == 0 or itime == ntime-1 ) :
            print(tmp)
            print(tmp.year)
            print(tmp.month)
            print(tmp.day)

    print(field.shape)
#
#   wavelength_bnds
    nwvl=len(wavelength)

    wavelength_bnds=np.zeros(nwvl+1, dtype=float)

    iwvl=0
    wavelength_bnds[iwvl]=wavelength[iwvl] - 0.5 * wavelength_width[iwvl]
    for iwvl in range(1,nwvl) :
        wvl0 = wavelength[iwvl-1] + 0.5 * wavelength_width[iwvl-1]
        wvl1 = wavelength[iwvl  ] - 0.5 * wavelength_width[iwvl  ]
        if ( wvl0 == wvl1 ) : 
            wavelength_bnds[iwvl] = wvl0
        else :
            print('+++ readspectrum_cdr +++')
            print('Lower and upper approach differ : ',wvl0, wvl1)
            quit()
#
    data = {'variable' : var, \
            'field' : field, \
            'units' : units, \
            'wavelength' : wavelength, \
            'wavelength_bnds' : wavelength_bnds, \
            'wavelength_units' : wavelength_units, \
            'yearlist' : yearlist, \
            'monthlist' : monthlist, \
            'decimalyearlist' : decimalyearlist \
            }
#
    return data

         





