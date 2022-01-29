import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
D = np.random.normal(
  (3, 5, 4), # moyenne
  (1.25, 1.00, 1.25), # ecart-type
  (100, 3))

plt.boxplot(D)
plt.show()