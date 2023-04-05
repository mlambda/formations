from deckz.standalones import register_plot


def main(data_label: str) -> None:
    import matplotlib.pyplot as plt
    from numpy import exp, linspace, ndarray, pi, sqrt
    from numpy.random import permutation

    def gaussian(x: ndarray, mu: float, sigma: float) -> ndarray:
        return exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * sqrt(2 * pi))

    fig, ax = plt.subplots(figsize=(15, 15))

    x = linspace(-30, 80, 4000)

    sigma = 9
    f = 10 * gaussian(x, 10, sigma)
    g = 15 * gaussian(x, 38, 15)
    h = f + g

    ax.plot(x, f, c="r", label="$f(x)$", linewidth=4)
    ax.plot(x, g, "-.", c="g", label="$g(x)$", linewidth=4)
    ind = permutation(len(x))[:200]
    ax.scatter(x[ind], h[ind], c="b", label=data_label)

    ax.legend(prop={"size": 30})


@register_plot()
def gaussian_mixture_univariate() -> None:
    main(data_label="Observations")


@register_plot()
def gaussian_mixture_univariate_en() -> None:
    main(data_label="Samples")
