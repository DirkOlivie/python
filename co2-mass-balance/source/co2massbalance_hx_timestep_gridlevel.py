import netCDF4 as nc
import datetime
import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc

def main():
#----------
#
    Rearth = 6370e3
#
    expid = 'n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.emisall.20260120c'
    dir   = '/datalake/NS9560K/noresm3/cases'

    species = 'CO2_LND'
#    species = 'CO2_OCN'

    hx         = 'h2i'

#   vervelende dates
    date0 = '2016-06-24-01800'
    date1 = '2019-10-02-01800'
    date2 = '2025-06-09-01800'
    date3 = '2032-10-28-01800'

    datelist=[date0, date1, date2, date3]

#   LOOP OVER ALL DATES
    for date in datelist :

        print('**************')
        print(date)
        print('**************')
        filename = dir+'/'+expid+'/atm/hist/'+expid+'.cam.'+hx+'.'+date+'.nc'
#

        area  = readnc.readnc('area',filename)*Rearth*Rearth        # m2
        TMCO2 = readnc.readnc('TM'+species,filename)  # read column burden
        SFCO2 = readnc.readnc('SF'+species,filename)  # read emissions 

        latitude = readnc.readnc('lat',filename)
        longitude=readnc.readnc('lon',filename)
#
        ncol = len(area)
#
        for i in range(48) : 
            TMCO2[i,:] = TMCO2[i,:] * area        * 1.e-12 # columnburden
            SFCO2[i,:] = SFCO2[i,:] * area * 1800 * 1.e-12 # emissions

        DIFFTMCO2 = TMCO2 * 0.
        DIFFTMCO2[1:48,:] = TMCO2[1:48,:] - TMCO2[0:47,:]

#       GLOBAL IMBALANCE
#        for i in range(1,48) :
#            print(i, np.sum(DIFFTMCO2[i,:]-SFCO2[i,:]), np.max(DIFFTMCO2[i,:]-SFCO2[i,:]), np.max(np.abs(SFCO2[i,:])))

#       LOCAL IMBALANCE
        for i in range(1,48) :
            for icol in range(0,ncol) :
                if ( np.abs(DIFFTMCO2[i,icol]-SFCO2[i,icol]) > 0.0005 ) :
                    print(i,icol, DIFFTMCO2[i,icol]-SFCO2[i,icol])
                    print(i,icol, DIFFTMCO2[i,icol]              )
                    print(i,icol,                  -SFCO2[i,icol])
                    print('lat : ', latitude[icol])
                    print('lon : ', longitude[icol])

#       print('SFCO2 : ', np.max(SFCO2), np.min(SFCO2), np.mean(SFCO2), np.mean(np.abs(SFCO2)))
        print('TMCO2 (diff) : ', np.max(DIFFTMCO2), np.min(DIFFTMCO2), np.mean(DIFFTMCO2), np.mean(np.abs(DIFFTMCO2)))

if __name__ == '__main__':
    main()
