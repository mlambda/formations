import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.ensemble
import sklearn.model_selection
import scipy.stats
import warnings
warnings.filterwarnings('ignore')

def preprocess(X):
    # Fill with median
    cols_1 = ['LotFrontage']
    X[cols_1] = X[cols_1].fillna(X[cols_1].median())

    # Fill with mode
    cols_2 = ['MSZoning', 'Electrical', 'KitchenQual',
              'Exterior1st', 'Exterior2nd', 'SaleType', 'Utilities']
    X[cols_2] = X[cols_2].fillna(X[cols_2].mode().iloc[0, :])

    #Fill with 'None'
    cols_3 = ['PoolQC', 'MiscFeature', 'Alley', 'Fence',
              'FireplaceQu', 'GarageQual', 'GarageCond',
              'GarageFinish', 'GarageType', 'BsmtQual', 'BsmtCond',
              'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
              'MasVnrType', 'MSSubClass']
    X[cols_3] = X[cols_3].fillna('None')

    # Fill with 0
    cols_4 = ['GarageYrBlt', 'GarageArea', 'GarageCars',
              'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF',
              'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath',
              'MasVnrArea']
    X[cols_4] = X[cols_4].fillna(0)

    # Other fills
    cols_5 = ['Functional']
    X[cols_5] = X[cols_5].fillna("Typ")

    # Some columns are ordinals, not numerical
    cols_num2ord = ['MSSubClass', 'OverallCond', 'YrSold', 'MoSold']
    X[cols_num2ord] = X[cols_num2ord].astype(str)

    X = X.replace({
        "Alley" : {"Grvl" : 1, "Pave" : 2},
        "BsmtCond" : {"None" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
        "BsmtExposure" : {"None" : 0, "Mn" : 1, "Av": 2, "Gd" : 3},
        "BsmtFinType1" : {"None" : 0, "Unf" : 1, "LwQ": 2, "Rec" : 3, "BLQ" : 4, "ALQ" : 5, "GLQ" : 6},
        "BsmtFinType2" : {"None" : 0, "Unf" : 1, "LwQ": 2, "Rec" : 3, "BLQ" : 4, "ALQ" : 5, "GLQ" : 6},
        "BsmtQual" : {"None" : 0, "Po" : 1, "Fa" : 2, "TA": 3, "Gd" : 4, "Ex" : 5},
        "ExterCond" : {"Po" : 1, "Fa" : 2, "TA": 3, "Gd": 4, "Ex" : 5},
        "ExterQual" : {"Po" : 1, "Fa" : 2, "TA": 3, "Gd": 4, "Ex" : 5},
        "FireplaceQu" : {"None" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
        "Functional" : {"Sal" : 1, "Sev" : 2, "Maj2" : 3, "Maj1" : 4, "Mod": 5, "Min2" : 6, "Min1" : 7, "Typ" : 8},
        "GarageCond" : {"None" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
        "GarageQual" : {"None" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
        "HeatingQC" : {"Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
        "KitchenQual" : {"Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
        "LandSlope" : {"Sev" : 1, "Mod" : 2, "Gtl" : 3},
        "LotShape" : {"IR3" : 1, "IR2" : 2, "IR1" : 3, "Reg" : 4},
        "PavedDrive" : {"None" : 0, "P" : 1, "Y" : 2},
        "PoolQC" : {"None" : 0, "Fa" : 1, "TA" : 2, "Gd" : 3, "Ex" : 4},
        "Street" : {"Grvl" : 1, "Pave" : 2},
        "Utilities" : {"ELO" : 1, "NoSeWa" : 2, "NoSewr" : 3, "AllPub" : 4}
    })

    return pd.get_dummies(X)
