from deckz.standalones import register_plot


@register_plot()
def simple():
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, np.pi * 2)
    y1 = np.cos(x)
    y2 = np.sin(x)

    plt.plot(x, y1)
    plt.plot(x, y2)
