# -----gridspecs-----
from matplotlib.gridspec import GridSpec

fig = plt.figure()
G = GridSpec(2, 3, figure=fig)
# Plor is put on the first spot
ax1 = plt.subplot(G[0, 0])
# Plot is put in a rectangular space 
# using multiple spots
ax2 = plt.subplot(G[0, 1:])
# ...
