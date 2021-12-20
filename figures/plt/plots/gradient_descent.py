from deckz.standalones import register_plot


class GradientDescent:
    def _make_surface(self, error_label: str) -> None:
        import matplotlib.pyplot as plt
        from numpy import cos, linspace, meshgrid, pi, sin

        self.xx, self.yy = meshgrid(
            linspace(-1, 1, 100), linspace(-2 * pi, 2 * pi, 100)
        )
        self.zz = (
            415 * sin(self.xx ** 2) + 3 * self.xx + 25 * self.yy + 50 * cos(self.yy)
        )

        fig, self.ax = plt.subplots(subplot_kw=dict(projection="3d"))

        self.ax.plot_surface(self.xx, self.yy, self.zz)
        self.ax.set(
            xlabel=r"$\theta_0$",
            ylabel=r"$\theta_1$",
            zlabel=error_label,
            xticklabels=[],
            yticklabels=[],
            zticklabels=[],
        )

    def plot_simple_gradient_descent(self, error_label: str) -> None:
        self._make_surface(error_label)
        m = [10, 20, 27, 35, 40, 45, 50, 50]
        n = [90, 80, 77, 75, 73, 72, 71, 21]
        self.ax.plot(
            self.xx[1, m[:-1]],
            self.yy[n[:-1], 1],
            self.zz[n[:-1], m[:-1]],
            "y^:",
            zorder=3,
        )
        self.ax.plot(
            self.xx[1, m[-1]],
            self.yy[n[-1], 1],
            self.zz[n[-1], m[-1]],
            "vr",
            zorder=3,
        )

    def plot_batch_methods(
        self,
        error_label: str,
        batch_label: str,
        mini_batch_label: str,
        stochastic_label: str,
    ) -> None:
        self._make_surface(error_label)
        m = [10, 35, 50]
        n = [90, 75, 71]
        self.ax.plot(
            self.xx[1, m],
            self.yy[n, 1],
            self.zz[n, m],
            "om-",
            label=batch_label,
            zorder=3,
        )
        m = [10, 12, 27, 60, 35, 60, 48, 50]
        n = [90, 75, 60, 50, 40, 35, 30, 21]
        self.ax.plot(
            self.xx[1, m],
            self.yy[n, 1],
            self.zz[n, m],
            "vr:",
            label=mini_batch_label,
            zorder=3,
        )
        m = [10, 40, 20, 19, 27, 60, 35, 18, 20, 25, 30, 45, 55, 50]
        n = [90, 80, 70, 60, 65, 58, 50, 40, 35, 25, 18, 10, 18, 21]
        self.ax.plot(
            self.xx[1, m],
            self.yy[n, 1],
            self.zz[n, m],
            "^y--",
            label=stochastic_label,
            zorder=3,
        )
        self.ax.legend()


@register_plot()
def gradient_descent() -> None:
    gradient_descent = GradientDescent()
    gradient_descent.plot_simple_gradient_descent(error_label="Erreur")


@register_plot()
def gradient_descent_en() -> None:
    gradient_descent = GradientDescent()
    gradient_descent.plot_simple_gradient_descent(error_label="Error")


@register_plot()
def batch_size_effect() -> None:
    gradient_descent = GradientDescent()
    gradient_descent.plot_batch_methods(
        error_label="Erreur",
        batch_label="Global",
        mini_batch_label="Batch",
        stochastic_label="Stochastique",
    )


@register_plot()
def batch_size_effect_en() -> None:
    gradient_descent = GradientDescent()
    gradient_descent.plot_batch_methods(
        error_label="Error",
        batch_label="Batch",
        mini_batch_label="Mini-batch",
        stochastic_label="Stochastic",
    )
