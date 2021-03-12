from pathlib import Path
from re import sub
from shutil import move

from yaml import dump

data = [
    [
        "Mise en évidence du surapprentissage",
        "",
        "",
        "overfitting-train-nzmog",
        "overfitting",
    ],
    [
        "Mise en évidence du surapprentissage",
        "",
        "",
        "overfitting-train-nzmog",
        "over-underfitting",
    ],
    [
        "Nuage de mots liés à l'intelligence artificielle",
        "",
        "",
        "data-science-nzmog",
        "data-science",
    ],
    [
        "Effet de la taille du batch",
        "",
        "",
        "batch-size-effect-nzmog",
        "batch-size-effect",
    ],
    [
        "Effet de l'écrêtage de gradient ",
        "",
        "",
        "gradient-clipping-nzmog",
        "gradient-clipping",
    ],
    [
        "Extension de la régression linéaire quand X est de dimension 2",
        "",
        "",
        "regression-hyperplan-nzmog",
        "regression-hyperplan",
    ],
    [
        "Surface de l'erreur en fonction des paramètres a et b",
        "",
        "",
        "gradient-nzmog",
        "gradient",
    ],
    [
        "Illustration des SVM à noyaux",
        "",
        "",
        "separable-problem-nonlinear-solution-nzmog",
        "separable-problem-nonlinear",
    ],
    [
        "Illustration des SVM à noyaux",
        "",
        "",
        "separable-problem-nonlinear-solution-nzmog",
        "separable-problem-nonlinear-solution",
    ],
    [
        "Illustration des SVM à noyaux",
        "",
        "",
        "separable-problem-nonlinear-kernelsvm-nzmog",
        "separable-problem-nonlinear-kernelsvm",
    ],
]


img_dir = Path("shared") / "img"
archive_dir = img_dir / "old"
archive_dir.mkdir(parents=True, exist_ok=True)

for title, author, license, new, old in data:
    if not author:
        author = r"F.-M. Giraud \& H. Mougard"
    if not license:
        license = "CC-BY-SA-4.0"
    with (img_dir / (f"{new}.yml" if new else f"{old}.yml")).open(
        mode="w", encoding="utf8"
    ) as fh:
        dump(
            dict(title=title, author=author, license=license),
            fh,
            allow_unicode=True,
        )
    if new != "" and new != old:
        pattern = fr'(\\V{{\[?"){old}(".*\]? \| image}})'
        for f in Path(".").glob("shared/latex/**/*.tex"):
            with f.open("r+", encoding="utf8") as fh:
                content = fh.read()
                fh.seek(0)
                fh.write(sub(pattern, fr"\1{new}\2", content))
                fh.truncate()
        for to_move in img_dir.glob(f"{old}.*"):
            if to_move.name.endswith(".yml") or to_move.name.endswith(".yaml"):
                continue
            move(str(to_move), str(archive_dir))
