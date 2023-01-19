import matplotlib.pyplot as plt

# -----sublplots-----
# 6 plots figure
# split on 2 lines and 3 columns
fig, ax = plt.subplots(2, 3)
# Plots can be accessed using their indexes
ax[0, 0].scatter(x1, y1)
ax[1, 0].scatter(x2, y2)
ax[0, 1].scatter(x2, y2)
# ...

# -----add_subplot-----
fig = plt.figure()
ax = fig.add_subplot(2, 3, 1)
ax.scatter(x, y)
ax = fig.add_subplot(2, 3, 2)
ax.scatter(x, y)
ax = fig.add_subplot(2, 3, 3)
ax.scatter(x, y)
# ...
