from deckz.standalones import register_plot
from mpl_toolkits.mplot3d import Axes3D

from .utils import Singleton


class NonLinearKernelSVM(metaclass=Singleton):
    def __init__(self) -> None:
        from numpy import linspace, meshgrid, ones
        from numpy.random import randn, uniform

        N = 300

        X = uniform(low=-1.0, high=1.0, size=(N, 2))
        self.x, self.y = X[:, 0], X[:, 1]
        self.xx, self.yy = meshgrid(linspace(-1, 1, 100), linspace(-1, 1, 100))
        self.R = 0.5
        bruit = 0
        self.classes = self.x ** 2 + self.y ** 2 < self.R ** 2 + bruit * randn(N)
        self.z = self.x ** 2 + self.y ** 2 + 1
        self.zz = 1.25 * ones(self.xx.shape)

        self.alpha = 0.6
        self.markersize = 2

    def _make_ax_and_plot_flat(self) -> Axes3D:
        import matplotlib.pyplot as plt
        from numpy import cos, linspace, pi, sin, zeros_like

        fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

        ax.view_init(elev=2, azim=0)
        ax.dist = 6
        ax.set(zlim=(0, self.z.max()), proj_type="persp")
        ax.set_axis_off()
        ax.plot(
            self.x[self.classes],
            self.y[self.classes],
            zeros_like(self.x)[self.classes],
            "b^",
            markersize=self.markersize,
            zorder=3,
            alpha=self.alpha,
        )
        ax.plot(
            self.x[~self.classes],
            self.y[~self.classes],
            zeros_like(self.x)[~self.classes],
            "rv",
            markersize=self.markersize,
            zorder=3,
            alpha=self.alpha,
        )
        t = linspace(0, 2 * pi, 100)
        ax.plot(
            self.R * cos(t),
            self.R * sin(t),
            zeros_like(t),
            "g",
            zorder=3,
            alpha=self.alpha,
        )
        return ax

    def plot_flat(self) -> None:
        self._make_ax_and_plot_flat()

    def plot_projection(self) -> None:
        ax = self._make_ax_and_plot_flat()

        ax.plot_surface(self.xx, self.yy, self.zz, color="g", alpha=self.alpha)
        ax.plot(
            self.x[self.classes],
            self.y[self.classes],
            self.z[self.classes],
            "b^",
            markersize=self.markersize,
            zorder=1,
            alpha=self.alpha,
        )
        ax.plot(
            self.x[~self.classes],
            self.y[~self.classes],
            self.z[~self.classes],
            "rv",
            markersize=self.markersize,
            zorder=3,
            alpha=self.alpha,
        )


@register_plot()
def separable_problem_nonlinear_solution() -> None:
    non_linear_kernel_svm = NonLinearKernelSVM()
    non_linear_kernel_svm.plot_flat()


@register_plot()
def separable_problem_nonlinear_kernelsvm() -> None:
    non_linear_kernel_svm = NonLinearKernelSVM()
    non_linear_kernel_svm.plot_projection()
