from deckz.standalones import register_plot

from .utils import Singleton


class Exploration(metaclass=Singleton):
    def __init__(self) -> None:
        from pathlib import Path

        from pandas import concat, get_dummies

        from .utils import load_csv

        train_df = load_csv(Path("ames") / "train", index_col="Id")
        test_df = load_csv(Path("ames") / "test", index_col="Id")

        train_X = train_df.drop(columns="SalePrice")
        self.train_y = train_df["SalePrice"]
        test_X = test_df
        all_X = concat([train_X, test_X])

        cols_1 = ["LotFrontage"]
        all_X[cols_1] = all_X[cols_1].fillna(train_X[cols_1].median())

        cols_2 = [
            "MSZoning",
            "Electrical",
            "KitchenQual",
            "Exterior1st",
            "Exterior2nd",
            "SaleType",
            "Utilities",
        ]
        all_X[cols_2] = all_X[cols_2].fillna(train_X[cols_2].mode().iloc[0, :])

        cols_4 = [
            "GarageYrBlt",
            "GarageArea",
            "GarageCars",
            "BsmtFinSF1",
            "BsmtFinSF2",
            "BsmtFullBath",
            "BsmtHalfBath",
            "BsmtUnfSF",
            "MasVnrArea",
            "TotalBsmtSF",
        ]
        all_X[cols_4] = all_X[cols_4].fillna(0)

        cols_5 = ["Functional"]
        all_X[cols_5] = all_X[cols_5].fillna("Typ")

        all_X = all_X.fillna("NA")

        cols_numerical2label = ["MSSubClass"]
        all_X[cols_numerical2label] = all_X[cols_numerical2label].astype(str)

        replace_mapping = dict(
            Alley=dict(NA=0, Grvl=1, Pave=2),
            BsmtExposure=dict(NA=0, No=1, Mn=2, Av=3, Gd=4),
            BsmtFinType1=dict(NA=0, Unf=1, LwQ=2, Rec=3, BLQ=4, ALQ=5, GLQ=6),
            BsmtFinType2=dict(NA=0, Unf=1, LwQ=2, Rec=3, BLQ=4, ALQ=5, GLQ=6),
            Functional=dict(Sal=1, Sev=2, Maj2=3, Maj1=4, Mod=5, Min2=6, Min1=7, Typ=8),
            LandSlope=dict(Sev=1, Mod=2, Gtl=3),
            LotShape=dict(IR3=1, IR2=2, IR1=3, Reg=4),
            PavedDrive=dict(NA=0, N=1, P=2, Y=3),
            Street=dict(Grvl=1, Pave=2),
            Utilities=dict(ELO=1, NoSeWa=2, NoSewr=3, AllPub=4),
        )
        quality_columns = [
            "BsmtCond",
            "BsmtQual",
            "ExterCond",
            "ExterQual",
            "FireplaceQu",
            "GarageCond",
            "GarageQual",
            "HeatingQC",
            "KitchenQual",
            "PoolQC",
        ]
        quality_mapping = dict(NA=0, Po=1, Fa=2, TA=3, Gd=4, Ex=5)
        for quality_column in quality_columns:
            replace_mapping[quality_column] = quality_mapping

        all_X.replace(replace_mapping, inplace=True)

        all_X = get_dummies(all_X)

        split_index = train_X.shape[0]
        self.train_X = all_X.iloc[:split_index, :]
        self.test_X = all_X.iloc[split_index:, :]

    def plot_hist(self, saleprice_label: str, count_label: str) -> None:
        from seaborn import histplot

        ax = histplot(self.train_y, kde=True, linewidth=0)
        ax.set(xlabel=saleprice_label, ylabel=count_label)

    def plot_hist_gaussian(self, saleprice_label: str, density_label: str) -> None:
        from numpy import linspace
        from scipy.stats import norm
        from seaborn import histplot

        ax = histplot(self.train_y, kde=True, linewidth=0, stat="density")
        ax.set(xlabel=saleprice_label, ylabel=density_label)
        mu, std = norm.fit(self.train_y)
        xx = linspace(*ax.get_xlim(), 100)  # type: ignore
        ax.plot(xx, norm.pdf(xx, mu, std), "k-")

    def plot_qq(self, quantiles_label: str, values_label: str) -> None:
        import matplotlib.pyplot as plt
        from scipy.stats import probplot

        _, ax = plt.subplots()
        probplot(self.train_y, dist="norm", plot=ax)
        ax.set(title=None, xlabel=quantiles_label, ylabel=values_label)

    def plot_corrmat(self, title: str) -> None:
        import matplotlib.pyplot as plt
        from seaborn import diverging_palette, heatmap

        sale_price_corrs = self.train_X.corrwith(self.train_y).sort_values().dropna()
        top_corrs_index = sale_price_corrs[-10:][::-1].index
        top_anticorrs_index = sale_price_corrs[:10].index
        index = top_corrs_index.union(top_anticorrs_index, sort=False)
        heatmap(
            self.train_X.loc[:, index].corr(),
            vmin=-1,
            vmax=1,
            cmap=diverging_palette(220, 20, n=100),
        )
        plt.title(title)

    def plot_scatter(self, area_label: str, saleprice_label: str) -> None:
        from seaborn import jointplot

        joint_grid = jointplot(x=self.train_X["GrLivArea"] / 10.764, y=self.train_y)
        joint_grid.ax_joint.set(xlabel=area_label, ylabel=saleprice_label)

    def plot_violin(self, quality_label: str, saleprice_label: str) -> None:
        from seaborn import violinplot

        ax = violinplot(x=self.train_X["OverallQual"], y=self.train_y)
        ax.set(xlabel=quality_label, ylabel=saleprice_label)

    def plot_bar(self, quality_label: str, saleprice_label: str) -> None:
        from seaborn import barplot

        ax = barplot(x=self.train_X["OverallQual"], y=self.train_y)
        ax.set(xlabel=quality_label, ylabel=saleprice_label)

    def plot_reg(self, area_label: str, saleprice_label: str) -> None:
        from seaborn import regplot

        ax = regplot(
            x=self.train_X["GrLivArea"] / 10.764,
            y=self.train_y,
            scatter_kws=dict(alpha=0.10),
            line_kws=dict(color="red"),
        )
        ax.set(xlabel=area_label, ylabel=saleprice_label)

    def plot_reglin_mse_loss(self, error_label: str) -> None:
        import matplotlib.pyplot as plt
        from numpy import linspace, meshgrid, zeros_like
        from sklearn.preprocessing import StandardScaler

        X = self.train_X[["GrLivArea"]].values
        Y = self.train_y.values[:, None]

        x_scaled = StandardScaler().fit_transform(X)[:, 0]
        y_scaled = StandardScaler().fit_transform(Y)[:, 0]

        def mse(theta_0: float, theta_1: float) -> float:
            return ((x_scaled * theta_1 + theta_0 - y_scaled) ** 2).mean()

        xx, yy = meshgrid(linspace(-4, 4, 100), linspace(-4, 4, 100))
        zz = zeros_like(xx)

        for i in range(xx.shape[0]):
            for j in range(xx.shape[1]):
                zz[i, j] = mse(xx[i, j], yy[i, j])

        fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
        ax.plot_surface(xx, yy, zz)

        ax.set(
            xlabel=r"$\theta_0$",
            ylabel=r"$\theta_1$",
            zlabel=error_label,
            xticklabels=[],
            yticklabels=[],
            zticklabels=[],
        )


@register_plot()
def histogram() -> None:
    exploration = Exploration()
    exploration.plot_hist(saleprice_label="Prix de vente ($)", count_label="Décompte")


@register_plot()
def histogram_en() -> None:
    exploration = Exploration()
    exploration.plot_hist(saleprice_label="Sale price ($)", count_label="Count")


@register_plot()
def histogram_gaussian() -> None:
    exploration = Exploration()
    exploration.plot_hist_gaussian(
        saleprice_label="Prix de vente ($)", density_label="Densité"
    )


@register_plot()
def histogram_gaussian_en() -> None:
    exploration = Exploration()
    exploration.plot_hist_gaussian(
        saleprice_label="Sale price ($)", density_label="Density"
    )


@register_plot()
def qq_plot() -> None:
    exploration = Exploration()
    exploration.plot_qq(
        quantiles_label="Quantiles théoriques", values_label="Prix de vente triés ($)"
    )


@register_plot()
def qq_plot_en() -> None:
    exploration = Exploration()
    exploration.plot_qq(
        quantiles_label="Theoretical quantiles", values_label="Ordered sale prices ($)"
    )


@register_plot()
def corrmat() -> None:
    exploration = Exploration()
    exploration.plot_corrmat(title="Plus grandes corrélations et anti-corrélations")


@register_plot()
def corrmat_en() -> None:
    exploration = Exploration()
    exploration.plot_corrmat(title="Biggest correlations and anti-correlations")


@register_plot()
def scatter_plot() -> None:
    exploration = Exploration()
    exploration.plot_scatter(
        area_label="Surface (m²)", saleprice_label="Prix de vente ($)"
    )


@register_plot()
def scatter_plot_en() -> None:
    exploration = Exploration()
    exploration.plot_scatter(
        area_label="Ground area (m²)", saleprice_label="Sale price ($)"
    )


@register_plot()
def violin_plot() -> None:
    exploration = Exploration()
    exploration.plot_violin(
        quality_label="Qualité globale", saleprice_label="Prix de vente ($)"
    )


@register_plot()
def violin_plot_en() -> None:
    exploration = Exploration()
    exploration.plot_violin(
        quality_label="Global quality", saleprice_label="Sale price ($)"
    )


@register_plot()
def bar_plot() -> None:
    exploration = Exploration()
    exploration.plot_bar(
        quality_label="Qualité globale", saleprice_label="Prix de vente ($)"
    )


@register_plot()
def bar_plot_en() -> None:
    exploration = Exploration()
    exploration.plot_bar(
        quality_label="Global quality", saleprice_label="Sale price ($)"
    )


@register_plot()
def reg_plot() -> None:
    exploration = Exploration()
    exploration.plot_reg(area_label="Surface (m²)", saleprice_label="Prix de vente ($)")


@register_plot()
def reg_plot_en() -> None:
    exploration = Exploration()
    exploration.plot_reg(
        area_label="Ground area (m²)", saleprice_label="Sale price ($)"
    )


@register_plot()
def linear_regression_error_surface() -> None:
    exploration = Exploration()
    exploration.plot_reglin_mse_loss(error_label="Erreur quadratique moyenne")


@register_plot()
def linear_regression_error_surface_en() -> None:
    exploration = Exploration()
    exploration.plot_reglin_mse_loss(error_label="Mean squared error")
