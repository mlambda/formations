import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 5., 0.2)
# r-- red dashes
# bs  blue squares
# g^  green triangles
plt.plot(t, t,
         'r--', t,
         t**2, 'bs',
         t, t**3, 'g^')
plt.show()
