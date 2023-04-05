from deckz.standalones import register_plot


def main(
    complexity_label: str,
    error_label: str,
    optimum_label: str,
    train_label: str,
    validation_label: str,
):
    import matplotlib.pyplot as plt
    from numpy import linspace

    fig, ax = plt.subplots(figsize=(15, 15))

    x = linspace(0, 5, 1000)
    y = 3 / (x + 1) ** 2 + x / 4

    ax.plot(x, y, c="g", label=validation_label, linewidth=4)

    y = 3 / (x + 1) ** 2
    ax.plot(x, y, "--", c="b", label=train_label, linewidth=4)
    ax.plot([1.884499, 1.884499], [0, 0.831687178], ":", c="r", linewidth=4)

    ax.annotate(
        optimum_label,
        xy=[1.884499, 0.831687178],
        xytext=(15, -60),
        textcoords="offset points",
        fontsize=30,
        ha="left",
        va="top",
        arrowprops=dict(
            arrowstyle="->",
            color="black",
            linewidth=0.75,
            connectionstyle="arc3,rad=0.2",
            shrinkB=20,
            relpos=(0.5, 1),
        ),
    )

    ax.set_xlabel(complexity_label, fontsize=30)
    ax.set_ylabel(error_label, fontsize=30)
    ax.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
    ax.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)

    ax.legend(prop={"size": 30})


@register_plot()
def learning_curve():
    main(
        complexity_label="Complexité",
        error_label="Erreur",
        optimum_label="Optimum",
        train_label="Train",
        validation_label="Validation",
    )


@register_plot()
def learning_curve_en():
    main(
        complexity_label="Complexity",
        error_label="Error",
        optimum_label="Optimum",
        train_label="Train",
        validation_label="Validation",
    )


@register_plot()
def early_stopping():
    main(
        complexity_label="Nombre d'itérations",
        error_label="Erreur",
        optimum_label="Optimum",
        train_label="Train",
        validation_label="Validation",
    )


@register_plot()
def early_stopping_en():
    main(
        complexity_label="Number of iterations",
        error_label="Error",
        optimum_label="Optimum",
        train_label="Train",
        validation_label="Validation",
    )
