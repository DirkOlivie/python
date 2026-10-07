import netCDF4 as nc
import numpy as np

def timelist2yearlistmonthlist(timelist, time_units, calendar):
#-----------------------------
    '''


    '''
    ntime=len(timelist)

#   new variables
    yearlist     = np.zeros(ntime, dtype=int)
    monthlist    = np.zeros(ntime, dtype=int) 

#
    for itime in range(len(timelist)) :

        datetime = nc.num2date(timelist[itime], time_units, calendar=calendar)

        yearlist[ itime] = datetime.year
        monthlist[itime] = datetime.month


    return yearlist, monthlist
