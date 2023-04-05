from typing import Any

from deckz.standalones import register_plot


# We'd rather say -> matplotlib.pyplot.Axes but we don't want to pay the import cost
def _work(prop: bool = False) -> Any:
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, np.pi * 4, 1000)
    y1 = np.cos(x)
    y2 = np.sin(x)

    if prop:
        plt.figure(figsize=(4, 8), dpi=100)
    else:
        plt.figure()

    ax = plt.subplot(1, 1, 1)

    ax.plot(x, y1)
    ax.plot(x, y2)

    return ax


@register_plot()
def classique_start() -> None:
    _work(prop=True)


@register_plot()
def spines() -> None:
    ax = _work()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


@register_plot()
def limits() -> None:
    from numpy import pi

    ax = _work()
    ax.set_ylim(0, 1)
    ax.set_xlim(0, pi * 2)


@register_plot()
def labels() -> None:
    ax = _work()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")


@register_plot()
def ticks() -> None:
    from numpy import pi

    ax = _work()
    ax.set_xlim(0, pi * 2)
    ax.set_xticks([0, pi / 2, pi, 3 * pi / 2, 2 * pi])
    ax.set_xticklabels([r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
