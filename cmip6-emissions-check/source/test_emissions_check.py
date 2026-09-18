import matplotlib.pyplot as plt
import os
import numpy as np
from netCDF4 import Dataset

import read_emissions_series

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction

#
# AIM
#   calculating global means of emissions fikes    
#
#

def test_emissions_check(filelist, sectorsum, code) :
#----------------------------------------------------    
#
#   read all files
    nfile=len(filelist)

    data = []

    for file in filelist :
#
#       find all variables in file
        nc_fid= Dataset(file, 'r')

#       list of all variables in file
        tmpvarlist=list(nc_fid.variables.keys())

#       will be list wiht good variables (3 dimensions)
        varlist=[] 
#       check number of dimensions for each variable         
        for tmpvar in tmpvarlist : 

           field=np.array(nc_fid.variables[tmpvar][:])
           
           if ( field.ndim == 3) : 

              varlist.append(tmpvar)
 
        nc_fid.close()
#
#       read individual fields
        for var in varlist :
            a = read_emissions_series.read_emissions_series(file=file,variable=var)

            data.append(a)

    nline=len(data)       
    print(nline)
    print(data[0])

# plotting
    fig, ax = plt.subplots(figsize=[8,4],dpi=100)
    ax.set_xlabel('Time [yr]')
    ax.set_ylabel('[Tg yr-1]') # use first experiment to obtain units
    ax.set_title('Emissions')

    for iline in range(0,nline) :
        ax.plot(data[iline]['timelist'], data[iline]['valuelist'], label = data[iline]['variable'])

    ax.legend()    

    path='/projects/NS2345K/www/people/olivie/plots'
    if  not os.path.isdir(path) : os.mkdir(path)

    fig.savefig(path+'/test_cmip6_emissions_'+code+'.ps' , bbox_inches='tight')
    fig.savefig(path+'/test_cmip6_emissions_'+code+'.png', bbox_inches='tight')
