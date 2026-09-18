import cartopy.crs as ccrs
import matplotlib.pyplot as plt

import os, sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import regiondefinition

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlregion

'''
https://scitools.org.uk/cartopy/docs/v0.15/matplotlib/intro.html
'''

fig = plt.figure(figsize=[10,10],dpi=100)

ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
ax.stock_img()

ny_lon, ny_lat = -75, 43
delhi_lon, delhi_lat = 77.23, 28.61

#plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
#         color='blue', linewidth=2, marker='o',
#         transform=ccrs.Geodetic(),
#         )

regionlist=['NORTHATL', 'INDIANOCN', 'BAYOFBENGA', 'NORTHATL2', 'SOUTHOCNIO', 'SOUTHOCNNF', 'TROPEASTPAC', 'TROPWESTPAC']

for region in regionlist :

    info=regiondefinition.getregiondefinition(region=region)

    x0=info['lonA']
    x1=info['lonB']
    y0=info['latA']
    y1=info['latB']

    xlist=[x0,x1,x1,x0,x0]
    ylist=[y0,y0,y1,y1,y0]


    plt.plot(xlist, ylist,
         color='blue', linewidth=2,
         transform=ccrs.PlateCarree(),
         )

    plt.text(x0, y0, getidlregion.getidlregion(region=region)+'  ',
         horizontalalignment='right',
         transform=ccrs.Geodetic()) 


#plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
#         color='gray', linestyle='--',
#         transform=ccrs.PlateCarree(),
#         )

#plt.text(ny_lon - 3, ny_lat - 12, 'New York',
#         horizontalalignment='right',
#         transform=ccrs.Geodetic())

#plt.text(delhi_lon + 3, delhi_lat - 12, 'Delhi',
#         horizontalalignment='left',
#         transform=ccrs.Geodetic())

#plt.show()

fig.savefig('/projects/NS2345K/www/people/olivie/plots/map_probeer.png', bbox_inches='tight')
fig.savefig('/projects/NS2345K/www/people/olivie/plots/map_probeer.ps' , bbox_inches='tight')

plt.close("all")
