from typing import Optional, Tuple, Union

from deckz.standalones import register_plot
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

        seed(42)

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
        epochs = 2_000
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

        model_nn.fit(
            self.X_train,
            self.y_train,
            epochs=epochs,
            batch_size=1024,
            callbacks=[
                keras.callbacks.EarlyStopping(monitor="loss", patience=patience),
                keras.callbacks.ModelCheckpoint(
                    filepath="overfitting_best_model.h5",
                    monitor="accuracy",
                    mode="max",
                    save_weights_only=True,
                    save_best_only=True,
                ),
            ],
        )
        model_nn.load_weights("overfitting_best_model.h5")

        Z_nn = model_nn.predict(to_predict)
        self.zz_nn = Z_nn.reshape(self.xx.shape)
        self.linewidth = 3

    def plot_all(
        self,
        train_title: str,
        all_title: str,
        label_svm: str,
        label_nn: str,
        hidden_label: str,
    ) -> None:
        fig, ax1, ax2 = self._setup_plot(  # type: ignore
            hidden_label=hidden_label,
            train_title=train_title,
            all_title=all_title,
        )
        self._add_contours(ax1, label_nn=label_nn, label_svm=label_svm)
        self._add_contours(ax2)
        ax1.legend(loc="lower right")

    def plot_train(self, label_svm: str, label_nn, hidden_label: str) -> None:
        fig, ax1 = self._setup_plot(
            also_plot_all_data=False, hidden_label=hidden_label
        )  # type: ignore
        self._add_contours(ax1, label_nn=label_nn, label_svm=label_svm)
        ax1.legend(loc="upper right")

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

        # Data points scatter plot(s)
        ax1.scatter(
            self.X_train[:, 0],
            self.X_train[:, 1],
            s=30,
            c=self.y_train,
            cmap=plt.cm.rainbow,
            edgecolors="k",
        )

        if also_plot_all_data:
            ax2.scatter(
                self.X[:, 0],
                self.X[:, 1],
                s=30,
                c=self.y,
                cmap=plt.cm.rainbow,
                edgecolors="k",
            )

        # Hidden function
        ax1.plot(
            numpy_sort(self.X[:, 1]),
            numpy_sort(self.X[:, 1]) ** 2 + -0.4,
            linewidth=self.linewidth,
            c="g",
            label=hidden_label,
        )

        if also_plot_all_data:
            ax2.plot(
                numpy_sort(self.X[:, 1]),
                numpy_sort(self.X[:, 1]) ** 2 + -0.4,
                linewidth=self.linewidth,
                c="g",
            )

        if also_plot_all_data:
            return fig, ax1, ax2
        else:
            return fig, ax1

    def _add_contours(
        self, ax: Axes, label_svm: Optional[str] = None, label_nn: Optional[str] = None
    ):
        contours = ax.contour(
            self.xx,
            self.yy,
            self.zz_svm,
            levels=[0.5],
            linewidths=self.linewidth,
            colors="b",
        )
        if label_svm is not None:
            contours.collections[0].set_label(label_svm)
        contours = ax.contour(
            self.xx,
            self.yy,
            self.zz_nn,
            levels=[0.5],
            linewidths=self.linewidth,
            colors="m",
        )
        if label_nn is not None:
            contours.collections[0].set_label(label_nn.format(n_hidden=self.n_hidden))


@register_plot()
def overfitting() -> None:
    overfitting = Overfitting()
    overfitting.plot_all(
        train_title="Données d'entraînement",
        all_title="Toutes les données",
        label_svm="SVM à noyau linéaire",
        label_nn="Réseau de neurones à {n_hidden} couches cachées",
        hidden_label="Fonction cachée",
    )


@register_plot()
def overfitting_train() -> None:
    overfitting = Overfitting()
    overfitting.plot_train(
        label_svm="SVM à noyau linéaire",
        label_nn="Réseau de neurones à {n_hidden} couches cachées",
        hidden_label="Fonction cachée",
    )
