import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import season2monthnumberlist


def fillzonalseriesstatistics (data, freqtype, season) :
#----------------------------
    '''
    AIM
        doing the correct average to obtain 'seasonalcycle','seasonalseries','monthlyseries','annualseries'

    INPUT
	    data     : contains whole timeseries - all years and months
 	    freqtype : 'seasonalcycle','seasonalseries','monthlyseries','annualseries'
        season   : [only relevant if annualseries - not implemented yet]

    MODIFICATIONS   
    2022-01-31

    '''

    print('+++ fillzonalseriesstatistics +++')
    print(freqtype)
    
    nmonth=12
#
    nlat  = data['nlat']
    ntime = data['ntime']
    print(data['ntime'])

# 1. creating monthly series
    if ( freqtype == 'monthlyseries' ) :

       x = np.zeros((ntime,nlat),dtype=float)  # time
       for ilat in range(0,nlat) : 
           x[:,ilat] = data['yearlist'] * 1. + data['monthlist'] *1. / 12. # decimal dates : 1850.08, 1850.16, ...

       y = np.zeros((ntime,nlat),dtype=float)  # latitude
       for itime in range(0,ntime) :
           y[itime,:] = data['latitude'] 
       
       z = data['valuelist']                   # actual value 

       units_time='year'

# 2. creating annual mean
    elif ( freqtype == 'annualseries' ) : 
        nyear = int (data['ntime'] / nmonth )
   
        year0=np.amin(data['yearlist'])
        year1=np.amax(data['yearlist'])

        year_annavg =np.zeros((nyear),     dtype=int)   # empty array for year 
        value_annavg=np.zeros((nyear,nlat),dtype=float)  # empty array for data

        for iyear in range(0,nyear) :
 
            year=year0 + iyear  

            boolarr = ( data['yearlist'] == year )

            year_annavg[iyear]  = year

            for ilat in range(0,nlat) :
                value_annavg[iyear,ilat] = np.mean(data['valuelist'][boolarr,ilat]) # average from 12 months -> 1 annual value

        x = np.zeros((nyear,nlat),dtype=int)   # time
        for ilat in range(0,nlat) :
            x[:,ilat] = year_annavg

        y = np.zeros((nyear,nlat),dtype=float) # latitudes 
        for itime in range(0,nyear) :
            y[itime,:] = data['latitude']

        z = value_annavg
        units_time='year'    
#
# 3. creating series of seasonal mean
    elif ( freqtype == 'seasonalseries' ) : 
        nyear = int (data['ntime'] / nmonth )
   
        year0=np.amin(data['yearlist'])
        year1=np.amax(data['yearlist'])

        year_seasonavg =np.zeros((nyear),     dtype=int)   # empty array for year 
        value_seasonavg=np.zeros((nyear,nlat),dtype=float)  # empty array for data

        for iyear in range(0,nyear) :

            year=year0 + iyear

            year_seasonavg[iyear]  = year

        monthlist=season2monthnumberlist.season2monthnumberlist(season=season) 
        ncontribution=len(monthlist)

        for month in monthlist : # accumulating over all contributing months

            boolarr = ( data['monthlist'] == month )
            print('+++')
            print(len(boolarr))
            print(len(data['valuelist'])) 

            value_seasonavg[:,:] = value_seasonavg[:,:] + data['valuelist'][boolarr,:]

        value_seasonavg = value_seasonavg / float(ncontribution)

        x = np.zeros((nyear,nlat),dtype=int)   # time
        for ilat in range(0,nlat) :
            x[:,ilat] = year_seasonavg

        y = np.zeros((nyear,nlat),dtype=float) # latitude
        for itime in range(0,nyear) :
            y[itime,:] = data['latitude']

        z = value_seasonavg                    # values
        units_time='year'    
#
# 4. creating seasonal cycle
    elif ( freqtype == 'seasonalcycle' ) :
        Ex_cycle   =np.zeros((nmonth,nlat), dtype=float)
        Exx_cycle  =np.zeros((nmonth,nlat), dtype=float)
        sigma_cycle=np.zeros((nmonth,nlat), dtype=float)
#
        for imonth in range(0,nmonth) :
#
           month=imonth+1 
#
           boolarr = ( data['monthlist'] == month )
           print(boolarr)
#
           for ilat in range(0,nlat) : 
               a = np.squeeze(data['valuelist'][0:ntime,ilat])
               print(len(a))
               print(len(boolarr))
               a = a[boolarr]

               Ex_cycle[imonth,ilat]    = np.mean(a) 
               Exx_cycle[imonth,ilat]   = np.mean(a*a)
               sigma_cycle[imonth,ilat] = np.sqrt(Exx_cycle[imonth,ilat]-Ex_cycle[imonth,ilat]*Ex_cycle[imonth,ilat])
#
        x = np.zeros((nmonth,nlat),dtype=int)   # time
        for ilat in range(0,nlat) :
            x[:,ilat] = range(1,nmonth+1)

        y = np.zeros((nmonth,nlat),dtype=float) # latitude
        for itime in range(0,nmonth) :
            y[itime,:] = data['latitude']

        z = Ex_cycle                            # values
        units_time='month'
#
# 5. creating output structure
#
    outdata = { 'expid'      : data['expid']   , \
                'variable'   : data['variable'], \
                'units'      : data['units']   , \
                'units_time' : units_time      , \
                'x' : x, \
                'y' : y, \
                'z' : z } 
#
    return outdata
