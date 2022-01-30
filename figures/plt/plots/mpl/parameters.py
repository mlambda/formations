from deckz.standalones import register_plot


def main(
    prop: bool = False,
    legend: bool = False,
    spines: bool = False,
    limits: bool = False,
    labels: bool = False,
    ticks: bool = False,
):
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, np.pi * 4, 1000)
    y1 = np.cos(x)
    y2 = np.sin(x)

    # Proportion, taille et résolution
    if prop:
        plt.figure(figsize=(4, 8), dpi=100)
    else:
        plt.figure()

    # Nouveau graphe (ligne, colonne,index)
    ax = plt.subplot(1, 1, 1)

    ax.plot(x, y1)
    ax.plot(x, y2)

    if legend:
        ax.legend(["cos", "sin"])
        ax.set_title("Cosinus et Sinus")

    if spines:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    if limits:
        ax.set_ylim(0, 1)
        ax.set_xlim(0, np.pi * 2)

    if labels:
        ax.set_xlabel("X")
        ax.set_ylabel("Y")

    if ticks:
        ax.set_xlim(0, np.pi * 2)
        ax.set_xticks(
            [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
        )
        ax.set_xticklabels([r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])


@register_plot()
def classique_start():
    main(prop=True)


@register_plot()
def legend():
    main(legend=True)


@register_plot()
def spines():
    main(spines=True)


@register_plot()
def limits():
    main(limits=True)


@register_plot()
def labels():
    main(labels=True)


@register_plot()
def ticks():
    main(ticks=True)
