from deckz.standalones import register_plot


def main() -> None:
    import matplotlib.pyplot as plt
    from numpy import linspace, meshgrid, ones, ones_like
    from numpy.random import permutation, randn

    bruit = 0.20
    N = 50

    X, Y = meshgrid(linspace(-1, 1, 100), linspace(-1, 1, 100))
    Z = ones_like(X)
    Z = 0.5 * X + 0.5 * Y
    XX = X.ravel()
    YY = Y.ravel()
    ZZ = Z.ravel()
    ind = permutation(len(XX))[:N]

    XX = XX[ind]
    YY = YY[ind]
    ZZ = ZZ[ind]
    ZZ2 = ZZ + bruit * randn(len(ZZ))

    _, ax = plt.subplots(subplot_kw=dict(projection="3d"))
    ax.set(xticklabels=[], yticklabels=[], zticklabels=[])
    ax.plot_surface(X, Y, Z, color="g", alpha=0.7)

    pos = ZZ2 > ZZ
    neg = ~pos

    for i in range(len(XX)):
        x = ones(2) * XX[i]
        y = ones(2) * YY[i]
        z = ones(2) * ZZ[i]
        z[1] = ZZ2[i]
        ax.plot3D(x, y, z, "b:", zorder=1 if z[1] < ZZ[i] else 3, linewidth=0.8)

    ax.plot3D(XX[pos], YY[pos], ZZ2[pos], "r^", zorder=3, markersize=2)
    ax.plot3D(XX[neg], YY[neg], ZZ2[neg], "r^", zorder=1, markersize=2)


@register_plot()
def regression_hyperplan() -> None:
    main()
