from deckz.standalones import register_plot


def _work(
    roc_curve_label: str,
    fpr_label: str,
    tpr_label: str,
    random_classifier_label: str,
    perfect_classifier_label: str,
) -> None:
    import matplotlib.pyplot as plt
    from sklearn import datasets
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import auc, roc_curve
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    # Load the breast cancer data set
    bc = datasets.load_breast_cancer()
    X, y = bc.data, bc.target

    # Create training and test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=1, stratify=y
    )

    # Create the estimator - pipeline
    pipeline = make_pipeline(StandardScaler(), LogisticRegression(random_state=1))

    # Create training test splits using two features
    pipeline.fit(X_train[:, [2, 13]], y_train)
    probs = pipeline.predict_proba(X_test[:, [2, 13]])
    fpr1, tpr1, thresholds = roc_curve(y_test, probs[:, 1], pos_label=1)
    roc_auc1 = auc(fpr1, tpr1)

    # Create training test splits using two different features
    pipeline.fit(X_train[:, [4, 14]], y_train)
    probs2 = pipeline.predict_proba(X_test[:, [4, 14]])
    fpr2, tpr2, thresholds = roc_curve(y_test, probs2[:, 1], pos_label=1)
    roc_auc2 = auc(fpr2, tpr2)

    # Create training test splits using all features
    pipeline.fit(X_train, y_train)
    probs3 = pipeline.predict_proba(X_test)
    fpr3, tpr3, thresholds = roc_curve(y_test, probs3[:, 1], pos_label=1)
    roc_auc3 = auc(fpr3, tpr3)

    fig, ax = plt.subplots(figsize=(7.5, 7.5))

    plt.plot(fpr1, tpr1, label=f"{roc_curve_label} 1 (AUC = {roc_auc1:0.2f})")
    plt.plot(fpr2, tpr2, "-.", label=f"{roc_curve_label} 2 (AUC = {roc_auc2:0.2f})")
    plt.plot(
        fpr3,
        tpr3,
        linestyle=(0, (5, 1)),
        label=f"{roc_curve_label} 3 (AUC = {roc_auc3:0.2f})",
    )
    plt.plot([0, 1], [0, 1], "--r", label=random_classifier_label)
    plt.plot([0, 0, 1], [0, 1, 1], ":g", label=perfect_classifier_label)
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel(fpr_label)
    plt.ylabel(tpr_label)
    plt.legend(loc="lower right")


@register_plot()
def auc() -> None:
    _work(
        roc_curve_label="Courbe ROC",
        fpr_label="Taux de faux positifs",
        tpr_label="Taux de vrais positifs",
        random_classifier_label="Classifieur aléatoire",
        perfect_classifier_label="Classifieur parfait",
    )


@register_plot()
def auc_en() -> None:
    _work(
        roc_curve_label="ROC curve",
        fpr_label="False positive rate",
        tpr_label="True positive rate",
        random_classifier_label="Random classifier",
        perfect_classifier_label="Perfect classifier",
    )
