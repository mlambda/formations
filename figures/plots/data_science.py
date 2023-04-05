from typing import Iterable

from deckz.standalones import register_plot

from .utils import load_resource


def _work(lang: str, pages: Iterable[str]) -> None:
    from re import sub

    import matplotlib.pyplot as plt
    from wikipedia import page, set_lang
    from wordcloud import WordCloud

    set_lang(lang)

    stopwords = frozenset(
        load_resource(f"stopwords/{lang}").decode("utf8").splitlines()
    )

    def wikip(query: str) -> str:
        wiki = page(query)
        text = wiki.content.lower()
        text = sub(r"==+.*?==+", "", text)
        text = text.replace("\n", " ")
        text = sub(r"\b.'(.+?)\b", r"\1", text)
        return text

    text = " ".join(map(wikip, pages))

    wordcloud = WordCloud(
        width=3000,
        prefer_horizontal=0.7,
        height=2000,
        random_state=1,
        background_color="white",
        colormap="Dark2",
        collocations=True,
        stopwords=stopwords,
        max_words=120,
        min_word_length=3,
    ).generate(text)

    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis("off")


@register_plot()
def data_science() -> None:
    _work(
        lang="fr",
        pages=[
            "Science_des_données",
            "Apprentissage_automatique",
            "Intelligence_artificielle",
            "Réseau_de_neurones_artificiels",
            "Biais_algorithmique",
            "Algorithme",
            "Apprentissage_profond",
            "Apprentissage_supervisé",
            "Apprentissage_non_supervisé",
        ],
    )


@register_plot()
def data_science_en() -> None:
    _work(
        lang="en",
        pages=[
            "Data science",
            "Artificial intelligence",
            "Neural network",
            "Algorithmic bias",
            "Algorithm",
            "Deep learning",
            "Supervised learning",
            "Unsupervised learning",
        ],
    )
