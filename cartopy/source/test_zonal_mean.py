import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker

def main():

    cexpid='FC2010climo_f19_20210204_test1'
    var='O3'
    var='TREFHT'
    #var='NO2'
    year=7
    month=10
    year0=11
    year1=20
    season='DJF'

#cexpid='NHIST_f19_tn14_20190710'
#var='ozone'
#year=2000
#month=6

    

    camversion='cam'

# read different fields : temperature, pressure, ozone, hyai, hybi
    yyyy = str("%4.4i"% (year))
    mm = str("%2.2i"% (month))
    nc_f='/projects/NS2345K/noresm/olivie/vsls/'+cexpid+'/atm/hist/'+cexpid+'.'+camversion+'.h0.'+yyyy+'-'+mm+'.nc'
#nc_f='/projects/NS9560K/noresm/cases/'+cexpid+'/atm/hist/'+cexpid+'.'+camversion+'.h0.'+yyyy+'-'+mm+'.nc'

    nc_fid= Dataset(nc_f, 'r')

    lats=np.array(nc_fid.variables['lat'][:])  # latitudes
    lons=np.array(nc_fid.variables['lon'][:])  # longitudes
    ps=np.squeeze(np.array(nc_fid.variables['PS'][:])) # surface pressure
    hyai=np.array(nc_fid.variables['hyai'][:]) # hyai
    hybi=np.array(nc_fid.variables['hybi'][:]) # hybi
    field=np.squeeze(np.array(nc_fid.variables[var][:]))

    p0=np.array(nc_fid.variables['P0'][:]) # reference pressure

    units=nc_fid.variables[var].units
    units_ps=nc_fid.variables['PS'].units
    units_p0=nc_fid.variables['P0'].units

    nc_fid.close

# make zonal average : 
    nlev, nlat, nlon = field.shape
    print(nlev, nlat,nlon)

    zonalmeanfield=np.mean(field,axis=2) # over last dimension = lon
    zonalmeanps=np.mean(ps,axis=1)       # over last dimension = lon

# calculate x,y,z field
    x = np.zeros( (nlev, nlat) )
    y = np.zeros( (nlev, nlat) )
    z = np.zeros( (nlev, nlat) )

    for ilev in range (nlev) :
        for ilat in range (nlat) :

            x[ilev,ilat] = lats[ilat]
            y[ilev,ilat] = p0 * hyai[ilev] + zonalmeanps[ilat] * hybi[ilev]
            z[ilev,ilat] = zonalmeanfield[ilev,ilat] 

    fig =  plt.figure(figsize=[10,10],dpi=100)
    ax = fig.add_subplot(1, 1, 1, ylim=(100000,100),yscale='log')
    ax.set_title(r'O$_3$')
    ax.set_xlabel('Longitude [deg]') # did not happen
    ax.set_ylabel('Pressure [Pa]')


#v = np.arange(0,1.e-5,1.e-6) # (start, stop, step) 
#v=np.array([0.01,0.02,0.05,0.1,0.2,0.5,1.0,2.0,5.0,10.0])*1.e-9

    filled_c = ax.contourf(x, y, z)
    #filled_c = ax.contourf(x, y, z, v)

    # And black line contours.
    line_c = ax.contour(x, y, z, levels=filled_c.levels, colors=['black'])



    # Add a colorbar for the filled contour.
    #fig.colorbar(filled_c, orientation='horizontal', label=units, aspect=40, shrink=0.8)
    fig.colorbar(filled_c, orientation='horizontal', aspect=40, shrink=1.0, format='%9.1e')

    # Use the line contours to place contour labels.
    ax.clabel(
        line_c,  # Typically best results when labelling line contours.
        colors=['black'],
        manual=False,  # Automatic placement vs manual placement.
        inline=True,  # Cut the line where the label will be placed.
        fmt=' {:.2e} '.format,  # Labes as integers, with some extra space.
    )

    #plt.show()
    fig.savefig('/projects/NS2345K/www/people/olivie/plots/'+var+cexpid+'.png')
