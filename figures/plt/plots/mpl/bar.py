from deckz.standalones import register_plot


def main():
    import matplotlib.pyplot as plt
    import numpy as np

    x = 0.5 + np.arange(8)
    y = np.random.uniform(2, 7, len(x))

    plt.bar(x, y)

@register_plot()
def bar():
    main()


