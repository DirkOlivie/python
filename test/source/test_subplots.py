import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
from matplotlib import colors

# Create 2x2 panel layout
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

x = np.random.rand(10)
y1 = np.random.rand(10)
y2 = np.random.rand(10)
y3 = np.random.rand(10)
y4 = np.random.rand(10)

data1 = np.random.rand(10, 10)
data2 = np.random.rand(10, 10)
norm = colors.Normalize(vmin=0, vmax=1)


# Plot on individual panels
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Panel 1')
axs[0, 1].scatter(x, y2)
axs[1, 0].bar(x, y3)
axs[1, 1].plot(data1)
#axs[1, 1] = plt.axes(projection=ccrs.PlateCarree())
#axs[1,1].coastlines()

fig.suptitle('Precipitation change', fontsize=16)

plt.tight_layout()
#plt.show()

fig.savefig('probeer_subplots.ps')#, bbox_inches='tight')
