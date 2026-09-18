import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from matplotlib import colors

# Define a layout with named panels
fig = plt.figure(figsize=(8, 8))
gs = fig.add_gridspec(7, 2)

# 1. Prepare data and shared normalization
data1 = np.random.rand(10, 10)
data2 = np.random.rand(10, 10)
norm = colors.Normalize(vmin=0, vmax=1)

# Panel 1: Map (Top Row)
ax_map = fig.add_subplot(gs[0:2, :], projection=ccrs.PlateCarree())
ax_map.coastlines()
ax_map.set_title("Geographic Map")
im = ax_map.imshow(data1, transform=ccrs.PlateCarree(), norm=norm, extent=[-180, 180, -70, 70], cmap='BrBG')

# plot line
lons = [-74.006, 2.3522]  # NY, Paris
lats = [40.7128, 48.8566]
ax_map.plot(lons, lats, color='blue', linewidth=2, marker='o', \
        transform=ccrs.Geodetic())



# Panel 2: XY Plot (Bottom Left)
ax_xy1 = fig.add_subplot(gs[2, 0])
ax_xy1.plot([1, 2, 3], [4, 5, 6])
ax_xy1.set_title("Data Series A")

# Panel 3: XY Plot (Bottom Right)
ax_xy2 = fig.add_subplot(gs[2, 1])
ax_xy2.scatter([1, 2, 3], [6, 5, 4])
ax_xy2.set_title("Data Series B")

# Panel 4: Map (Bottom Row)
ax_map4 = fig.add_subplot(gs[3:5, 0], projection=ccrs.PlateCarree())
ax_map4.coastlines()
ax_map4.set_title("Geographic Map")
im = ax_map4.imshow(data1, transform=ccrs.PlateCarree(), norm=norm, extent=[-180, 180, -70, 70], cmap='BrBG')
gl = ax_map4.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.top_labels = False   # Disable top labels
gl.right_labels = False # Disable right labels



# Panel 5: Map (Bottom Row)
ax_map5 = fig.add_subplot(gs[3:5, 1], projection=ccrs.PlateCarree())
ax_map5.coastlines()
ax_map5.set_title("Geographic Map")
im = ax_map5.imshow(data2, transform=ccrs.PlateCarree(), norm=norm, extent=[-180, 180, -70, 70], cmap='BrBG')
gl = ax_map5.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.top_labels = False   # Disable top labels
gl.right_labels = False # Disable right labels

# Panel 6: XY Plot (Bottom Left)
ax_xy1 = fig.add_subplot(gs[5, 0])
ax_xy1.plot([1, 2, 3], [4, 5, 6])
ax_xy1.set_title("Data Series A")

# Panel 7: XY Plot (Bottom Right)
ax_xy2 = fig.add_subplot(gs[5, 1])
ax_xy2.scatter([1, 2, 3], [6, 5, 4])
ax_xy2.set_title("Data Series B")

# Panel 8 : colorbar
#cax = fig.add_subplot(gs[6, :])


#cax = fig.add_axes([0.1, 0.05, 0.9, 0.05]

cax = fig.add_axes([0.12, 0.06, 0.76, 0.02])
fig.colorbar(im, cax=cax, orientation='horizontal',extend='both', label=r'$\Delta_3$'+'Precipitation')#, fraction=0.05, pad=0.1, extend='both', label=r'$\Delta_3$'+'Precipitation')

fig.suptitle('Precipitation change', fontsize=16)


plt.tight_layout()

fig.savefig('probeer_mosaic_orig.ps')
