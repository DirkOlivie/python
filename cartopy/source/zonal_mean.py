"""
========
Colorbar
========

Use `~.figure.Figure.colorbar` by specifying the mappable object (here
the `~.matplotlib.image.AxesImage` returned by `~.axes.Axes.imshow`)
and the axes to attach the colorbar to.
"""

import numpy as np
import matplotlib.pyplot as plt

# setup some generic data
N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))

# mask out the negative and positive values, respectively
Zpos = np.ma.masked_less(Z, 0)
Zneg = np.ma.masked_greater(Z, 0)

fig, (ax1, ax2, ax3) = plt.subplots(figsize=(13, 6), ncols=3)

# plot just the positive data and save the
# color "mappable" object returned by ax1.imshow
pos = ax1.imshow(Zpos, cmap='Blues', interpolation='none')

# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which axes object it should be near
fig.colorbar(pos, ax=ax1)
ax1.set_title('Cold values')
ax1.set_xlabel('Latitude [deg]')
ax1.set_ylabel('Height (hPa]')
line_c = ax1.contour(y,x,Zpos,levels=[0.25, 0.50,0.75,1.00,1.25,1.50,1.75],colors=['black'])
ax1.grid(b=True, which='major', color='r', linestyle='--', linewidth=0.5)


# repeat everything above for the negative data
# you can specify location, anchor and shrink the colorbar
neg = ax2.imshow(Zneg, cmap='Reds_r', interpolation='none')
#fig.colorbar(neg, ax=ax2, location='right', anchor=(0, 0.3), shrink=0.7)
fig.colorbar(neg, ax=ax2, anchor=(0, 0.3), shrink=0.7) # location did not work

# Plot both positive and negative values between +/- 1.2
pos_neg_clipped = ax3.imshow(Z, cmap='RdBu', vmin=-1.2, vmax=1.2,
                             interpolation='none')
# Add minorticks on the colorbar to make it easy to read the
# values off the colorbar.
cbar = fig.colorbar(pos_neg_clipped, ax=ax3, extend='both')
cbar.minorticks_on()
#plt.show()
fig.savefig('/projects/NS2345K/www/people/olivie/plots/zonalmean.png')
