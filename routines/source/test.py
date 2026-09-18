import numpy as np
import intplon
import intplat
import interp1d


print('LONGITUDES')
loninbd=np.arange(13)*30.-180.
lonoutbd=np.arange(7)*60.
print(loninbd)
print(lonoutbd)

a,b = intplon.intplon(loninbd=loninbd, lonoutbd=lonoutbd)
a
b

print('LATITUDES')
latinbd=np.arange(19)*10.-90.
latoutbd=np.arange(10)*20.-90.
print(latinbd)
print(latoutbd)

a,b = intplat.intplat(latinbd=latinbd, latoutbd=latoutbd)

print(a)
print(b)

print('LEVELS')
x=np.arange(10)*10.
y=np.arange(20)*5.
fx=np.arange(10)*10. + 4.

fy=interp1d.interp1d(x=x,y=y,fx=fx)

print(x)
print(y)
print(fx)
print(fy)
