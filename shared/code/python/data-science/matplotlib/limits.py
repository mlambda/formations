import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,np.pi*4,1000)
y1=np.cos(x)
y2=np.sin(x)

fig=plt.figure()
ax=plt.subplot(1,1,1)

# Limites d'affichage
ax.set_ylim(0,1)
ax.set_xlim(0,np.pi*2)

ax.plot(x,y1)
ax.plot(x,y2)

plt.show()