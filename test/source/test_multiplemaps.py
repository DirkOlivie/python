# https://matplotlib.org/stable/gallery/images_contours_and_fields/multi_image.html


import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from matplotlib import colors

# Coordinate Reference Systems (CRS)
# PlateCarree, Mercator, Miller
# LambertConformal, AlbersEqualArea
# Orthographic, Stereographic, Gnomonic
# Mollweide, Robinson, Sinusoidal


# 1. Prepare data and shared normalization
data1 = np.random.rand(10, 10)
data2 = np.random.rand(10, 10)
norm = colors.Normalize(vmin=0, vmax=1)

# 2. Create subplots with Cartopy projection
fig, axs = plt.subplots(1, 2, figsize=(10, 4), 
                        subplot_kw={'projection': ccrs.Mollweide()})
#                        subplot_kw={'projection': ccrs.PlateCarree()})

fig.suptitle('Precipitation', fontsize=16)

# 3. Plot maps using the same norm
for i, (ax, data) in enumerate(zip(axs, [data1, data2])):
    ax.coastlines()
    # Store the mappable (im) to use for the colorbar
    im = ax.imshow(data, transform=ccrs.PlateCarree(), norm=norm, extent=[-180, 180, -70, 70], cmap='BrBG')
    ax.set_title(f'Map hallo {i+1}')
    
    gl = ax.gridlines(draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
    gl.top_labels = False   # Disable top labels
    gl.right_labels = False # Disable right labels


# 4. Add common colorbar across all specified axes
fig.colorbar(im, ax=axs, orientation='horizontal', fraction=0.05, pad=0.1, extend='both', label=r'$\Delta_3$'+'Precipitation')

fig.suptitle('Precipitation change', fontsize=16)

fig.savefig('probeer_multiplemaps3.ps', bbox_inches='tight')
