from deckz.standalones import register_plot


@register_plot()
def scatter() -> None:
    import matplotlib.pyplot as plt
    import numpy as np

    rng = np.random.default_rng()

    x = rng.normal(size=250)
    y = rng.normal(size=250)

    plt.scatter(x, y)
