from deckz.standalones import register_plot


@register_plot()
def hist():
    import matplotlib.pyplot as plt
    import numpy as np

    rng = np.random.default_rng()
    x = rng.normal(4, size=1000)

    plt.hist(x, bins=10)
