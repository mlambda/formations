from deckz.standalones import register_plot


def main():
    import matplotlib.pyplot as plt
    import numpy as np

    x=np.random.normal(4,size=1000)

    plt.hist(x, bins=10)

@register_plot()
def hist():
    main()


