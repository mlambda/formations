from deckz.standalones import register_plot


def main(error_label: str) -> None:
    import matplotlib.pyplot as plt
    from numpy import cos, linspace, meshgrid, pi, sin

    X, Y = meshgrid(linspace(-1, 1, 100), linspace(-1 * 2 * pi, 1 * 2 * pi, 100))
    Z = 415 * sin(X ** 2) + 3 * X + 25 * Y + 50 * cos(Y)

    fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

    ax.plot_surface(X, Y, Z)

    m = [10, 20, 27, 35, 40, 45, 50, 50]
    n = [90, 80, 77, 75, 73, 72, 71, 21]
    ax.plot(
        X[1, m[:-1]],
        Y[n[:-1], 1],
        Z[n[:-1], m[:-1]],
        "y^:",
        zorder=3,
    )
    ax.plot(
        X[1, m[-1]],
        Y[n[-1], 1],
        Z[n[-1], m[-1]],
        "vr",
        zorder=3,
    )
    ax.set(
        xlabel=r"$\theta_0$",
        ylabel=r"$\theta_1$",
        zlabel=error_label,
        xticklabels=[],
        yticklabels=[],
        zticklabels=[],
    )


@register_plot()
def gradient_descent() -> None:
    main(error_label="Erreur")


@register_plot()
def gradient_descent_en() -> None:
    main(error_label="Error")
