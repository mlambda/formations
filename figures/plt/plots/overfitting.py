from os.path import join as path_join
from tempfile import TemporaryDirectory
from typing import Optional, Tuple, Union

from deckz.standalones import register_plot
from matplotlib.artist import Artist
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from plots.utils import Singleton


class Overfitting(metaclass=Singleton):
    def __init__(self) -> None:

        from numpy import c_, linspace, meshgrid
        from numpy.random import randn, seed, uniform
        from sklearn.model_selection import train_test_split
        from sklearn.svm import LinearSVC
        from tensorflow import keras
        from tensorflow.random import set_seed

        seed(42)
        set_seed(42)

        # Création des données
        N = 300

        self.X = uniform(low=-1.0, high=1.0, size=(N, 2))

        X0, X1 = self.X[:, 0], self.X[:, 1]
        self.y = X1 > X0 ** 2 - 0.4 + 0.5 * randn(N)

        self.X_train, _, self.y_train, _ = train_test_split(
            self.X, self.y, test_size=0.4, random_state=42
        )

        self.xx, self.yy = meshgrid(linspace(-1, 1, 500), linspace(-1, 1, 500))

        to_predict = c_[self.xx.ravel(), self.yy.ravel()]

        # Entraînement du SVM
        model_svm = LinearSVC()
        model_svm.fit(self.X_train, self.y_train)
        Z_svm = model_svm.decision_function(to_predict)
        self.zz_svm = Z_svm.reshape(self.xx.shape)

        # Entraînement du NN
        hidden_size = 50
        self.n_hidden = 10
        epochs = 3_000
        patience = 50
        learning_rate = 1e-4

        model_nn = keras.Sequential(
            [
                keras.layers.Dense(
                    hidden_size, activation="relu", kernel_initializer="orthogonal"
                )
                for _ in range(self.n_hidden)
            ]
        )
        model_nn.add(
            keras.layers.Dense(1, activation="sigmoid", kernel_initializer="orthogonal")
        )

        model_nn.compile(
            optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
            loss="binary_crossentropy",
            metrics=["accuracy"],
        )
        with TemporaryDirectory() as tmpdirname:
            best_model_path = path_join(tmpdirname, "overfitting_best_model.h5")
            model_nn.fit(
                self.X_train,
                self.y_train,
                epochs=epochs,
                batch_size=1024,
                callbacks=[
                    keras.callbacks.EarlyStopping(monitor="loss", patience=patience),
                    keras.callbacks.ModelCheckpoint(
                        filepath=best_model_path,
                        monitor="accuracy",
                        mode="max",
                        save_weights_only=True,
                        save_best_only=True,
                    ),
                ],
            )
            model_nn.load_weights(best_model_path)

        Z_nn = model_nn.predict(to_predict)
        self.zz_nn = Z_nn.reshape(self.xx.shape)
        self.linewidth = 2

    def plot_all(
        self,
        train_title: str,
        all_title: str,
        svm_label: str,
        nn_label: str,
        hidden_label: str,
    ) -> None:
        fig, ax1, ax2 = self._setup_plot(  # type: ignore
            hidden_label=hidden_label,
            train_title=train_title,
            all_title=all_title,
        )
        svm_artist, nn_artist = self._add_contours(ax1)
        self._add_contours(ax2)
        handles, labels = ax1.get_legend_handles_labels()
        ax1.legend(
            handles + [svm_artist, nn_artist],
            labels + [svm_label, nn_label.format(n_hidden=self.n_hidden)],
            loc="upper right",
            markerscale=2,
        )

    def plot_train(self, svm_label: str, nn_label: str, hidden_label: str) -> None:
        fig, ax1 = self._setup_plot(
            also_plot_all_data=False, hidden_label=hidden_label
        )  # type: ignore
        svm_artist, nn_artist = self._add_contours(ax1)
        handles, labels = ax1.get_legend_handles_labels()
        ax1.legend(
            handles + [svm_artist, nn_artist],
            labels + [svm_label, nn_label.format(n_hidden=self.n_hidden)],
            loc="upper right",
            handlelength=5,
        )

    def _initialize_ax(self, ax: Axes, title: Optional[str]) -> None:
        ax.set_xticks([])
        ax.set_yticks([])
        if title is not None:
            ax.set_title(title)

    def _setup_plot(
        self,
        also_plot_all_data: bool = True,
        hidden_label: str = "Fonction cachée",
        train_title: Optional[str] = None,
        all_title: Optional[str] = None,
    ) -> Union[Tuple[Figure, Axes, Axes], Tuple[Figure, Axes]]:
        import matplotlib.pyplot as plt
        from numpy import sort as numpy_sort

        if also_plot_all_data:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
            plt.subplots_adjust(wspace=0.05, hspace=0)
            self._initialize_ax(ax1, title=train_title)
            self._initialize_ax(ax2, title=all_title)
        else:
            fig, ax1 = plt.subplots(figsize=(6, 5))
            self._initialize_ax(ax1, title=train_title)

        y0_train_mask = self.y_train == 0
        y1_train_mask = self.y_train == 1
        y0_mask = self.y == 0
        y1_mask = self.y == 1

        # Data points scatter plot(s)
        ax1.plot(
            self.X_train[:, 0][y0_train_mask],
            self.X_train[:, 1][y0_train_mask],
            "bv",
            markersize=2,
        )

        ax1.plot(
            self.X_train[:, 0][y1_train_mask],
            self.X_train[:, 1][y1_train_mask],
            "r^",
            markersize=2,
        )

        if also_plot_all_data:
            ax2.plot(
                self.X[:, 0][y0_mask],
                self.X[:, 1][y0_mask],
                "bv",
                markersize=2,
            )

            ax2.plot(
                self.X[:, 0][y1_mask],
                self.X[:, 1][y1_mask],
                "r^",
                markersize=2,
            )

        # Hidden function
        ax1.plot(
            numpy_sort(self.X[:, 1]),
            numpy_sort(self.X[:, 1]) ** 2 + -0.4,
            "--k",
            linewidth=self.linewidth,
            label=hidden_label,
        )

        if also_plot_all_data:
            ax2.plot(
                numpy_sort(self.X[:, 1]),
                numpy_sort(self.X[:, 1]) ** 2 + -0.4,
                "--k",
                linewidth=self.linewidth,
            )

        if also_plot_all_data:
            return fig, ax1, ax2
        else:
            return fig, ax1

    def _add_contours(self, ax: Axes) -> Tuple[Artist, Artist]:
        contours_svm = ax.contour(
            self.xx,
            self.yy,
            self.zz_svm,
            linestyles="dotted",
            levels=[0],
            linewidths=self.linewidth,
            colors="g",
        )
        contours_nn = ax.contour(
            self.xx,
            self.yy,
            self.zz_nn,
            levels=[0.5],
            linewidths=0.5,
            colors="m",
        )
        ax.contourf(
            self.xx,
            self.yy,
            self.zz_nn,
            levels=[0, 0.5, 1],
            colors=[(0, 0, 1, 0.07), (1, 0, 0, 0.07)],
        )
        return contours_svm.legend_elements()[0][0], contours_nn.legend_elements()[0][0]


@register_plot()
def overfitting() -> None:
    overfitting = Overfitting()
    overfitting.plot_all(
        train_title="Données d'entraînement",
        all_title="Toutes les données",
        svm_label="SVM à noyau linéaire",
        nn_label="Réseau de neurones à {n_hidden} couches cachées",
        hidden_label="Fonction cachée",
    )


@register_plot()
def overfitting_train() -> None:
    overfitting = Overfitting()
    overfitting.plot_train(
        svm_label="SVM à noyau linéaire",
        nn_label="Réseau de neurones à {n_hidden} couches cachées",
        hidden_label="Fonction cachée",
    )
