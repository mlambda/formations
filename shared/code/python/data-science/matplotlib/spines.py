import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi * 4, 1000)
y1 = np.cos(x)
y2 = np.sin(x)

fig, ax = plt.subplots()

# Modification des spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.plot(x, y1)
ax.plot(x, y2)

fig.show()
