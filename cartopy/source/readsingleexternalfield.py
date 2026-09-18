import numpy as np
from netCDF4 import Dataset
import getoxidcliminfo
import getozonecliminfo

def readsingleexternalfield (expid, var, date, climtype) :
#--------------------------
    '''
    INPUT
        expid
        var
        date
        climtype

	date : format = 'yyyy-mm'
        type : 'oxidant' or 'ozone'

    MODIFICATIONS
        (2024-04-26) extensions to radiative ozone climatology
                        added climtype to allow for distinction between oxidants and (radiative) ozone

    '''
# disentangle the date
    line=date.split("-")
    year=int(line[0])
    month=int(line[1]) 

# get the external field
    if ( climtype == 'oxidant' ) :
        climinfo = getoxidcliminfo.getoxidcliminfo(expid=expid)  
    elif ( climtype == 'ozone' ) :
        climinfo = getozonecliminfo.getozonecliminfo(expid=expid) 
     
    if ( climinfo['method'] == 'cyclical' ) : 
        year_search = climinfo['cycleyear']         
    elif ( climinfo['method'] == 'interp_missing_months' ) :
        year_search = year 
     
#   extract data from NetCDF file     
    nc_f=climinfo['filename']
    print(nc_f)
    nc_fid= Dataset(nc_f, 'r')                 # open for reading
    lats=np.array(nc_fid.variables['lat'][:])  # latitudes
    lons=np.array(nc_fid.variables['lon'][:])  # longitudes

    hyai=np.array(nc_fid.variables['hyai'][:]) # hyai
    hybi=np.array(nc_fid.variables['hybi'][:]) # hybi

    hyam=np.array(nc_fid.variables['hyam'][:]) # hyam
    hybm=np.array(nc_fid.variables['hybm'][:]) # hybm

    p0=np.array(nc_fid.variables['P0'][:])     # reference pressure
    ps=np.array(nc_fid.variables['PS'][:])     # reference pressure
    ps_unit=nc_fid.variables['PS'].units

    datelist=nc_fid.variables['date'][:]        # read dates    

    field=np.squeeze(np.array(nc_fid.variables[var][:])) # read variable
    units=nc_fid.variables[var].units                 # read units
    units_ps=nc_fid.variables['PS'].units                 # read units
    units_p0=nc_fid.variables['P0'].units                 # read units

    nc_fid.close

    ntime, nlev, nlat, nlon= field.shape # CORRECT ORDER?
#
    ntime = len(datelist)   
    yearlist = np.floor_divide(datelist , 10000)
    monthlist = np.mod( np.floor_divide(datelist , 100) , 100 )
#
    print(datelist)
    print(yearlist)
    print(monthlist)

#   find infimum and supremum date        
    itimeA=-1
    for itime in range(0,ntime) :
        if ( yearlist[itime] <= year_search and monthlist[itime] == month ) : itimeA=itime

    itimeB=ntime
    for itime in range(ntime-1,-1,-1) :
        if ( yearlist[itime] >= year_search and monthlist[itime] == month ) : itimeB=itime 

    print(year_search)
    print(itimeA)
    print(itimeB)

    yearA=yearlist[itimeA]
    yearB=yearlist[itimeB]

    print('year_search, yearA, yearB : ', year_search, yearA, yearB)

    if ( yearA == yearB ) :
        wA = 0.5
        wB = 0.5
    else : 
        wA = float(yearB - year_search) / float(yearB - yearA)
        wB = float(year_search - yearA) / float(yearB - yearA)

    print('wA, wB : ', wA, wB)

    psA = ps[itimeA,:,:]
    psB = ps[itimeB,:,:]
    ps  = wA * psA + wB *psB

#    print(ps)
#    quit()

    fieldA = field[itimeA,:,:,:]
    fieldB = field[itimeB,:,:,:] 
    
    field = wA * fieldA + wB * fieldB

#   return data
    data = { 'longitude' : lons, \
             'latitude'  : lats, \
             'field'     : field, \
             'units'     : units, \
             'units_ps'  : units_ps, \
             'units_p0'  : units_p0, \
             'ps' : ps, \
             'p0' : p0, \
             'hyam' : hyam,  \
             'hybm' : hybm, \
             'hyai' : hyai, \
             'hybi' : hybi}

    return data
