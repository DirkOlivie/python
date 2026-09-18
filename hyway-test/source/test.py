import numpy as np
import math

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc

dir='/projects/NS11106K/HYway/modelling_repository/NorESM2-LM-C/transient2010s'

farea=dir+'/areacella_fixed_NorESM2-LM-C_hyway.nc'
fvolume=dir+'/volume_monthly_NorESM2-LM-C_hyway_transient2010s_r1i1p1f1_201001-201912.nc'
fairmass=dir+'/airmass_monthly_NorESM2-LM-C_hyway_transient2010s_r1i1p1f1_201001-201912.nc'
fch4=dir+'/ch4_monthly_NorESM2-LM-C_hyway_transient2010s_r1i1p1f1_201001-201912.nc'
flossch4=dir+'/lossch4_monthly_NorESM2-LM-C_hyway_transient2010s_r1i1p1f1_201001-201912.nc'

area    = readnc.readnc('areacella',farea)
volume  = readnc.readnc('volume',fvolume)
airmass = readnc.readnc('airmass',fairmass)
lossch4 = readnc.readnc('lossch4',flossch4)

print('area from file : ', np.sum(area))
print('area from formula : ', 4. * math.pi * 6370e3 * 6370e3)
print('lossch4 : ', np.sum(volume*lossch4, axis=(1,2,3))*86400.*365*1.e-9) 
print('mean height : ', np.sum(volume, axis=(1,2,3))/(4. * math.pi * 6370e3 * 6370e3))
print('airmass : ', np.sum(np.sum(np.mean(airmass, axis=0),axis=0)*area))


