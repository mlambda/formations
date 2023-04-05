from deckz.standalones import register_plot


@register_plot()
def bar() -> None:
    import matplotlib.pyplot as plt
    import numpy as np

    rng = np.random.default_rng()

    x = 0.5 + np.arange(8)
    y = rng.uniform(2, 7, len(x))

    plt.bar(x, y)
