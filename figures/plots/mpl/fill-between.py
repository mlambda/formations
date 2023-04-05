from deckz.standalones import register_plot


@register_plot()
def fill_between():
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, np.pi * 2)
    y1 = np.cos(x)
    y2 = np.sin(x)

    plt.fill_between(x, y1, 0, alpha=0.5)
    plt.fill_between(x, y2, 0, alpha=0.5)
