import matplotlib.pyplot as plt
import numpy as np

# -----sublplots-----
# Figure contenant 6 plots
# sur 2 lignes et 3 colonnes
fig,ax=plt.subplots(2,3)
# Accès à chaque plot par indice
ax[0,0].scatter(x1,y1)
ax[1,0].scatter(x2,y2)
ax[0,1].scatter(x2,y2)
# ...

# -----add_subplot-----
fig=plt.figure()
ax=fig.add_subplot(2,3,1)
ax.scatter(x,y)
ax=fig.add_subplot(2,3,2)
ax.scatter(x,y)
ax=fig.add_subplot(2,3,3)
ax.scatter(x,y)
# ...