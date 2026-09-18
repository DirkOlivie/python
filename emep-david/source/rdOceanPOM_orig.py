#!/usr/bin/env python3
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import sys

EARTH_RAD = 6378.1370    # earth equatorial radius, km, =a, WGS-84
RAD2 = EARTH_RAD*EARTH_RAD
deg2Rad = np.pi/180.0

def km2_areaLonLatCell(clat,dLat,dLon):
  """ area matches calculation based on spherical cap, e.g.
      http://mathforum.org/library/drmath/view/63767.html
      Also uses WGS-84 R """

  assert clat> -90.0 and clat<90,'emxgeo: Impossible lat %f' % clat
  drLon = dLon*deg2Rad
  rLat1 = (clat-0.5*dLat)*deg2Rad
  rLat2 = (clat+0.5*dLat)*deg2Rad
  S = RAD2*drLon*(np.sin(rLat2)-np.sin(rLat1))  # ie uses WGS-84
  return S



# ******************************* INPUT DIR:
idir='/home/davids/MDISKS/Nebula/work/Data/inputs_emis/NorEsmOceanicPOM'
idir='/projects/NS2345K/www/people/olivie/emep'
# *******************************

ds=xr.open_dataset(idir+'/emipomocean.NFHISTnorpddmsbcsdyn_standard_opom_f09_mg17_20210226.cam.h0.200101-201012-climo.nc')
pom=ds.emipomocean.values
pom12=np.mean(pom,axis=0)   # 12-monthly mean kg/m2/s, ignoring monthly differences in day numbers
lats=ds.lat.values
lons=ds.lon.values
dLon = lons[1]-lons[0]
dLat = lats[1]-lats[0]

print('Lons ', lons[0], lons[-1],  dLon )
print('Lats ', lats[0], lats[-1],  dLat )

esum = 0.0

for j, lat in enumerate(lats):
  if lat > 89.999: continue  # Can't process 90.0 N
  m2 = 1.0e6 * km2_areaLonLatCell(lat+0.5*dLat,dLat,dLon) 
  for i, lon in enumerate(lons):
      esum += (m2 * pom12[j,i])    # now kg/s

# 1 Gg = 1.0e6 kg
print('SUM Tg/yr', esum*3600*365.0* 1.0e-6 )
    
sys.exit()

plt.pcolormesh( np.sum(pom,axis=0) )
plt.colorbar()
plt.show()
#plt.pcolormesh(pom)



""" NCDUMP:
       lat = 192 ;
       lon = 288 ;
       time = UNLIMITED ; // (12 currently)
       float emipomocean(time, lat, lon) ;
       emipomocean:units = "kg/m2/s" ;
       emipomocean:long_name = "ocean POM surface flux" ;
       emipomocean:cell_methods = "time: mean" ;

General notes:
 emis anthropogenic POM ca. 5 TgC/yr, BB 11 TgC/yr  (Hallquist et al., 2009)
 Kirkevåg et al. 2018: Ocean OM flux tuned to 8 Tg/yr to match Spracklen et al 2008
"""


