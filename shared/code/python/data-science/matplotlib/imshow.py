import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(
    np.linspace(-3, 3, 256),
    np.linspace(-3, 3, 265))
Z = (1 - X / 2 + X ** 5 + Y ** 3) \
    * np.exp(-(X ** 2) - Y ** 2)

plt.imshow(Z)
plt.show()
