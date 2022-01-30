import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi * 4, 1000)
y1 = np.cos(x)
y2 = np.sin(x)

# Proportion, taille et résolution
# Récupération du nouveau graphe
fig, ax = plt.subplots(figsize=(4, 8),
                     dpi=100)

ax.plot(x, y1)
ax.plot(x, y2)

plt.show()
