import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(10)
D = rng.normal(
  (3, 5, 4),           # mean
  (1.25, 1.00, 1.25),  # standard deviation
  (100, 3))

plt.boxplot(D)
plt.show()
