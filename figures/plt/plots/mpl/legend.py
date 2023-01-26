from deckz.standalones import register_plot
import matplotlib.pyplot as plt
import numpy as np


@register_plot()
def legend():
    x = np.linspace(0, np.pi * 4, 1000)
    y1 = np.cos(x)
    y2 = np.sin(x)

    fig, ax = plt.subplots()

    ax.plot(x, y1, label="cos")
    ax.plot(x, y2, label="sin")

    ax.legend()

    ax.set_title("Cosinus et Sinus")

    fig.show()

