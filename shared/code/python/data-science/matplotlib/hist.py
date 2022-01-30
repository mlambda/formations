import matplotlib.pyplot as plt
import numpy as np

x=np.random.normal(4,size=1000)

plt.hist(x, bins=10)

plt.show()