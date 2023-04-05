from deckz.standalones import register_plot


def main(hidden_label: str, data_label: str, degree_label: str) -> None:
    import matplotlib.pyplot as plt
    from matplotlib.axes import Axes
    from numpy import linspace, ndarray, poly1d, polyfit
    from numpy.random import normal, seed
    from sklearn.metrics import mean_squared_error

    seed(42)

    def fit_poly(x: ndarray, y: ndarray, d: int) -> poly1d:
        return poly1d(polyfit(x, y, d))

    n = 15
    xmin = -4
    xmax = 4

    # Génération de 100000 nombres aléatoires
    x = linspace(xmin, xmax, n)
    # Génération de nos cibles
    y = -50 * x**3 + 10 * x**2 + 500 * x + normal(0, 150, len(x))

    preds_x = linspace(xmin, xmax, n * 1000)
    y_real = -50 * preds_x**3 + 10 * preds_x**2 + 500 * preds_x

    legend_size = 15
    title_font_size = 17

    def plot_polynomial(degree: int, ax: Axes) -> None:
        poly = fit_poly(x, y, degree)
        preds_y = poly(preds_x)
        ax.plot(preds_x, y_real, "--", c="g", label=hidden_label)
        ax.scatter(x, y, label=data_label)
        ax.plot(preds_x, preds_y, c="r", label=f"{degree_label} {poly.order}")
        rmse_obs = mean_squared_error(y, poly(x))
        rmse_true = mean_squared_error(y_real, preds_y)
        ax.set_title(
            f"MSE(Train)={rmse_obs:.2e} ; MSE(Test)={rmse_true:.2E}",
            fontsize=title_font_size,
        )

        ax.legend(prop={"size": legend_size})

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 5))
    plot_polynomial(1, ax1)
    plot_polynomial(3, ax2)
    plot_polynomial(15, ax3)


@register_plot()
def overfit_polynomial() -> None:
    main("Fonction cachée", "Observations", "Degré")


@register_plot()
def overfit_polynomial_en() -> None:
    main("Hidden function", "Training data", "Degree")
