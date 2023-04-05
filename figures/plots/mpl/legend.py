import matplotlib.pyplot as plt
import numpy as np
from deckz.standalones import register_plot


def _work(title: str) -> None:
    x = np.linspace(0, np.pi * 4, 1000)
    y1 = np.cos(x)
    y2 = np.sin(x)

    _, ax = plt.subplots()

    ax.plot(x, y1, label="cos")
    ax.plot(x, y2, label="sin")

    ax.legend()

    ax.set_title(title)


@register_plot()
def legend() -> None:
    _work("Cosinus et sinus")


@register_plot()
def legend_en() -> None:
    _work("Sine and cosine")
