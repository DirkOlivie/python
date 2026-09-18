import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# 1. Create a figure with subplots
# Use 'subplot_kw' to pass the projection to specific axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 5), 
                               subplot_kw={'projection': None})

# 2. Standard Matplotlib plot (ax1)
ax1.plot([0, 1, 2], [10, 20, 10], marker='o')
ax1.set_title('Standard Plot')

# 3. Cartopy map plot (ax2)
# We must re-create ax2 with a projection if subplots() didn't assign one
ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.PlateCarree())
ax2.set_global()
ax2.coastlines()
ax2.set_title('Cartopy Map')

plt.tight_layout()

fig.savefig('probeer_combination.ps')
