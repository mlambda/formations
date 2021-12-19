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


@register_plot()
def histplot() -> None:
    exploration = Exploration()
    exploration.plot_hist(saleprice_label="Prix de vente", count_label="Décompte")


@register_plot()
def histplot_en() -> None:
    exploration = Exploration()
    exploration.plot_hist(saleprice_label="Sale price", count_label="Count")
