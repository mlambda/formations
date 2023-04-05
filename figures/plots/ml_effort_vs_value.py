from typing import Any, Iterable, Mapping, Sequence, Tuple

from deckz.standalones import register_plot


def main(
    cost_label: str,
    benefit_label: str,
    tabular_title_label: str,
    deep_title_label: str,
    baseline_label: str,
    ml_label: str,
    dl_label: str,
) -> None:
    import matplotlib.pyplot as plt
    from matplotlib.axes import Axes

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    def setup_ax(
        ax: Axes,
        title: str,
        x: Sequence[float],
        y: Sequence[float],
        annotations: Iterable[Tuple[bool, Mapping[str, Any]]],
    ) -> None:
        ax.tick_params(
            axis="both",
            which="both",
            bottom=False,
            left=False,
            labelbottom=False,
            labelleft=False,
        )
        ax.set_xlim(-2, 130)
        ax.set_ylim(-2, 110)
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.spines["left"].set_position(("data", -10))
        ax.spines["bottom"].set_position(("data", -10))

        fontsize = 15

        ax.plot(x, y, "C1:o", linewidth=2, markersize=6)
        ax.set_xlabel(cost_label, fontsize=fontsize)
        ax.set_ylabel(benefit_label, fontsize=fontsize)
        ax.set_title(title, fontsize=fontsize + 5)
        for i, (pos_angle, annotation) in enumerate(annotations, start=1):
            ax.annotate(
                xy=(x[i], y[i]),
                textcoords="offset points",
                fontsize=fontsize - 5,
                arrowprops=dict(
                    arrowstyle="->",
                    color="black",
                    linewidth=0.75,
                    connectionstyle=f"arc3,rad={0.2 if pos_angle else -0.2}",
                    shrinkB=20,
                    relpos=(0.5, 1),
                ),
                **annotation,
            )

    setup_ax(
        ax1,
        title=tabular_title_label,
        x=[0, 20, 60, 110],
        y=[0, 20, 80, 83],
        annotations=[
            (True, dict(text=baseline_label, xytext=(15, -30), ha="left", va="top")),
            (False, dict(text=ml_label, xytext=(-45, -30), ha="right", va="top")),
            (True, dict(text=dl_label, xytext=(-45, 30), ha="right", va="bottom")),
        ],
    )
    setup_ax(
        ax2,
        title=deep_title_label,
        x=[0, 10, 60, 110],
        y=[0, 10, 90, 20],
        annotations=[
            (True, dict(text=baseline_label, xytext=(15, -30), ha="left", va="top")),
            (False, dict(text=dl_label, xytext=(-45, -30), ha="right", va="top")),
            (True, dict(text=ml_label, xytext=(-45, 30), ha="right", va="bottom")),
        ],
    )


@register_plot()
def ml_effort_vs_value() -> None:
    main(
        cost_label="Effort",
        benefit_label="Plus-value",
        tabular_title_label="Données tabulaires",
        deep_title_label="Images/sons/vidéos",
        baseline_label="Baseline de bon sens",
        ml_label="Machine Learning",
        dl_label="Deep Learning",
    )


@register_plot()
def ml_effort_vs_value_en() -> None:
    main(
        cost_label="Cost",
        benefit_label="Benefit",
        tabular_title_label="Tabular data",
        deep_title_label="Images/sounds/videos",
        baseline_label="Baseline",
        ml_label="Machine Learning",
        dl_label="Deep Learning",
    )
