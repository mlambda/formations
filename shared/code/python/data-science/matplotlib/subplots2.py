# -----gridspecs-----
from matplotlib.gridspec import GridSpec

fig = plt.figure()
G = GridSpec(2, 3, figure=fig)
# Le plot occupera 1 emplacement
ax1 = plt.subplot(G[0, 0])
# Le plot occupera une zone rectangulaire
# de plusieurs emplacement
ax2 = plt.subplot(G[0, 1:])
# ...
