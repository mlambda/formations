import matplotlib.pyplot as plt
import numpy as np
im = np.array(
    [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
)

plt.imshow(im,cmap='gray_r')
plt.show()