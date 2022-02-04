import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, np.pi * 4, 1000)
y1, y2 = np.cos(x), np.sin(x)

fig, ax = plt.subplots()
ax.set_xlim(0, np.pi * 2)

ax.set_xticks(  # Changement des ticks
    [0, np.pi / 2, np.pi, 3 * np.pi / 2,
     2 * np.pi])
ax.set_xticklabels([
    r"$0$", r"$\pi/2$", r"$\pi$",
    r"$3\pi/2$", r"$2\pi$"])

ax.plot(x, y1)
ax.plot(x, y2)
fig.show()
