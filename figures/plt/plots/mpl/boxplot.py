from deckz.standalones import register_plot


@register_plot()
def boxplot():
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(10)
    D = np.random.normal(loc=(3, 5, 4), scale=(1.25, 1.00, 1.25), size=(100, 3))

    plt.boxplot(D)
