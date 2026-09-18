from netCDF4 import Dataset
from datetime import datetime
import numpy as np
import math
import os
import matplotlib.pyplot as plt


import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getidlunits
import getstandardunits
import getpreviousdate


def analysedaily(expid, var, datelist, directory, calendar, code) :
#---------------

#   
#   timelist=np.arange(getpreviousdate.getpreviousdate(date=datelist[0], calendar=calendar),datelist[-1], dtype='datetime64[D]')
#    timelist=np.arange('0001-01-01',datelist[-2], dtype='datetime64[D]') # was introducing 29-02-2004 
#    print(len(datelist))
#    print(len(timelist))
#    print(timelist)
 

#   timelist=np.zeros(len(datelist), dtype='datetime64[D]')
    timelist=[] # will be used for plotting: lower date by -1 (average of 0018-01-01 is in file with name 0018-01-02)
    for i in range(0,len(datelist)) :
        timelist.append(datetime.fromisoformat(getpreviousdate.getpreviousdate(datelist[i],calendar=calendar)+'T12:00:00'))
        print(i, datelist[i], timelist[i])

#    quit()

    valuelist=[]

    for date in datelist :
        filename = directory+'/'+expid+'/atm/hist/'+expid+'.cam.h1a.'+date+'-00000.nc'

        nc_fid=Dataset(filename, 'r')


        if ( var == 'AODVISdivDAYFOC' ) : 
            field=np.squeeze(np.array(nc_fid.variables['AODVIS'][:])) / ( np.squeeze(np.array(nc_fid.variables['DAYFOC'][:])) + 1.e-20 )
            units=nc_fid.variables['AODVIS'].units
        else : 
            field=np.squeeze(np.array(nc_fid.variables[var][:]))
            units=nc_fid.variables[var].units

        units=getstandardunits.getstandardunits(units)

        area= np.squeeze(np.array(nc_fid.variables['area'][:]))
#       print('area : ', sum(area)) # sums to 12.566370614359078 

        areawt=np.squeeze(np.array(nc_fid.variables['areawt'][:]))
#       print('areawt : ', sum(areawt)) # sums to 1.0000

        nc_fid.close()

        globarea=4.*math.pi*6.37e6*6.37e6

        ytype = ''
        if ( units == 'kg m-2' ) : value=sum(field*areawt)*globarea *1.e-9 ; units='Tg' ; ytype='log' 
        elif ( units == 'W m-2') : value=sum(field*areawt)
        elif ( units == 'K'    ) : value=sum(field*areawt)-273.16 ; units='C'
        elif ( units == 'unitless' ) : value=sum(field*areawt) ; ytype='log'
        else : 
            print('No units recognized : ', units)
            quit()

        valuelist.append(value)

        print(date, value, units)

#   PLOT FIGURE
    fig, ax = plt.subplots(figsize=[6,3],dpi=200)

    ax.set_title(getidlvar.getidlvar(var))
    ax.set_xlabel('Time [year-month-day]')                                     # x-axis label 
    ax.set_ylabel('['+getidlunits.getidlunits(units=units)+']') # y-axis label
#
    if ( ytype == 'log' ) : ax.set_yscale('log')
#
#   ax.plot(datelist,valuelist)
    ax.plot(timelist,valuelist)
#   ax.plot(timelist,valuelist,marker='o')
#
    path='/projects/NS9560K/users/olivie/plots'
    if  not os.path.isdir(path) : os.mkdir(path)

    fig.savefig(path+'/'+var+'_daily_'+code+'.ps' , bbox_inches='tight')
    fig.savefig(path+'/'+var+'_daily_'+code+'.png', bbox_inches='tight')
