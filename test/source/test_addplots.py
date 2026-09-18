import matplotlib.pyplot as plt

fig = plt.figure()
# Standard plot
ax1 = fig.add_subplot(1, 3, 1) 
# Polar plot
ax2 = fig.add_subplot(1, 3, 2, projection='polar') 
# 3D plot
ax3 = fig.add_subplot(1, 3, 3, projection='3d')

fig.savefig('probeer2.ps')# , bbox_inches='tight')

