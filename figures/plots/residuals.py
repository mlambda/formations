from deckz.standalones import register_plot
from numpy import ndarray


def main(x: ndarray, y1: ndarray, y2: ndarray, y3: ndarray) -> None:
    import matplotlib.pyplot as plt
    from numpy import poly1d, polyfit, zeros

    fig, axs = plt.subplots(2, 3, figsize=(20, 10))

    def splothow(axs, x, y):
        top, bot = axs
        size = 3
        poly = poly1d(polyfit(x, y, 1))
        residuels = y - poly(x)
        top.plot(x, poly(x))
        top.scatter(x, y, s=size)
        bot.plot(x, zeros(len(x)), linestyle="dashed")
        bot.scatter(x, residuels, s=size)

    splothow(axs[:, 0], x, y1)
    splothow(axs[:, 1], x, y2)
    splothow(axs[:, 2], x, y3)


@register_plot()
def residuals_1() -> None:
    from numpy import linspace
    from numpy.random import normal

    x = linspace(-4, 4, 60)
    y1 = -1 * x + -3 + -normal(0, 1, len(x))
    y2 = -1 * x + -3 + -0.2 * x ** 2 - 0.5 * normal(0, 1, len(x))
    y3 = -1 * x + -3 + -normal(0, 3, len(x))
    main(x, y1, y2, y3)


@register_plot()
def residuals_2() -> None:
    from numpy import exp, linspace, minimum, multiply, ones, sin
    from numpy.random import normal

    x = linspace(0, 10, 60)
    y1 = -1 * x + -3 + multiply(x, sin(x) + normal(0, 0.3, len(x)))
    y2 = -1 * x + -3 + 0.05 * minimum(50 * ones(len(x)), exp(x)) * normal(0, 1, len(x))
    y3 = -10 * x ** 4 - normal(0, 3, len(x))
    main(x, y1, y2, y3)
