from deckz.standalones import register_plot


def main(
    degree_label: str,
):
    import matplotlib.pyplot as plt
    from numpy import linspace, multiply, poly1d, polyfit

    fig, ax = plt.subplots(figsize=(15, 15))

    n = 40

    x = linspace(0, 8, n)

    y = (
        multiply(
            [3.1415 * 2.7],
            [
                50,
                65,
                80,
                80,
                50,
                60,
                60,
                48,
                50,
                55,
                53,
                75,
                80,
                105,
                100,
                90,
                103,
                88,
                80,
                70,
                75,
                60,
                50,
                52,
                70,
                58,
                80,
                95,
                125,
                124,
                140,
                80,
                120,
                125,
                88,
                92,
                70,
                110,
                155,
                325,
            ],
        )
        - 400
    )

    preds_x = linspace(0, 8, n * 1000)

    for degree, fmt in [(3, "-.b"), (5, "--g"), (8, "r")]:
        poly = poly1d(polyfit(x, y, degree))
        ax.plot(
            preds_x,
            poly(preds_x),
            fmt,
            label=f"{degree_label} {degree}",
            linewidth=4,
        )

    ax.scatter(x, y, label="Data")
    ax.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)

    ax.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)

    ax.legend(prop={"size": 30})


@register_plot()
def polynomial_regression():
    main("Degré")


@register_plot()
def polynomial_regression_en():
    main("Degree")
