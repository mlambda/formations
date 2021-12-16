from datetime import datetime

from deckz.standalones import register_plot


def main(drivers_label: str, cnns_label: str) -> None:
    from io import StringIO
    from pkgutil import get_data

    import matplotlib.pyplot as plt
    from pandas import DataFrame, read_csv

    nvidia_path = "data/stock-prices/NVDA.csv"
    btc_path = "data/stock-prices/BTC-USD.csv"
    eth_path = "data/stock-prices/ETH-USD.csv"

    def load_csv(path: str) -> DataFrame:
        content = get_data(__name__, path)
        if content is None:
            raise RuntimeError(f"Could not load {path}")
        df = read_csv(
            StringIO(content.decode("utf8")), index_col="Date", parse_dates=True
        )
        df = df.resample("90d").mean()
        return df

    nvidia_df = load_csv(nvidia_path)
    plt.plot(nvidia_df.index, nvidia_df["Open"], label="NVIDIA")

    btc_df = load_csv(btc_path)
    plt.plot(btc_df.index, btc_df["Open"] / 100, "--", label="BTC/100")

    eth_df = load_csv(eth_path)
    plt.plot(eth_df.index, eth_df["Open"] / 10, "-.", label="ETH/10")

    cuda = datetime.fromisoformat("2007-06-23")
    catneuron = datetime.fromisoformat("2012-07-01")
    plt.plot([cuda, cuda], [0, 100], ":k")
    plt.annotate(drivers_label, (cuda, 115), ha="center")
    plt.plot([catneuron, catneuron], [0, 200], ":k")
    plt.annotate(cnns_label, (catneuron, 215), ha="center")
    plt.legend(prop={"size": 15})


@register_plot()
def nvidia_stock_history() -> None:
    main(drivers_label="Drivers CUDA", cnns_label="CNNs performants")


@register_plot()
def nvidia_stock_history_en() -> None:
    main(drivers_label="CUDA drivers", cnns_label="Efficient CNNs")
