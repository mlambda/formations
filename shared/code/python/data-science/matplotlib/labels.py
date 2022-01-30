import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi * 4, 1000)
y1 = np.cos(x)
y2 = np.sin(x)

fig, ax = plt.subplots()

# Label d'axe
ax.set_xlabel("X")
ax.set_ylabel("Y")

ax.plot(x, y1)
ax.plot(x, y2)

plt.show()
