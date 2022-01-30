import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,np.pi*4,1000)
y1=np.cos(x)
y2=np.sin(x)

fig=plt.figure()
ax=plt.subplot(1,1,1)

ax.set_xlim(0,np.pi*2)
# Changement des ticks
ax.set_xticks([0, np.pi/2, np.pi,
            3*np.pi/2, 2*np.pi],)
ax.set_xticklabels([r'$0$',
        r'$\pi/2$',r'$\pi$',
        r'$3\pi/2$', r'$2\pi$'])

ax.plot(x,y1)
ax.plot(x,y2)

plt.show()