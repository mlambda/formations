from deckz.standalones import register_plot


def main(positive: bool, slope_label: str):
    import matplotlib.pyplot as plt
    from numpy import linspace

    _, ax = plt.subplots(figsize=(6, 6))

    x = linspace(-1.3, 1.3, 100)
    y = x ** 2

    ax.plot(x, y, label="$f(x) = x^2$", linewidth=2)

    if positive:
        x_tan = linspace(0.5, 1.3, 50)
        y_tan = 2 * x_tan - 1
    else:
        x_tan = linspace(-1.3, -0.5, 50)
        y_tan = -2 * x_tan - 1
    ax.plot(x_tan, y_tan, "r--", label=slope_label, linewidth=2)

    marker = [1, 1] if positive else [-1, 1]
    ax.plot(*marker, "ro", label="$f(1)$" if positive else "$f(-1)$", markersize=5)

    ax.legend()


@register_plot()
def slope_positive():
    main(positive=True, slope_label="Pente / dérivée")


@register_plot()
def slope_positive_en():
    main(positive=True, slope_label="Slope / derivative")


@register_plot()
def slope_negative():
    main(positive=False, slope_label="Pente / dérivée")


@register_plot()
def slope_negative_en():
    main(positive=False, slope_label="Slope / derivative")
