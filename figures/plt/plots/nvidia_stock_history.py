from deckz.standalones import register_plot


def main(drivers_label: str, cnns_label: str) -> None:
    from datetime import datetime

    import matplotlib.pyplot as plt
    from pandas import DataFrame

    from .utils import load_csv

    def load_stock_csv(name: str) -> DataFrame:
        df = load_csv(
            f"data/stock-prices/{name}.csv", index_col="Date", parse_dates=True
        )
        df = df.resample("90d").mean()
        return df

    nvidia_df = load_stock_csv("NVDA")
    plt.plot(nvidia_df.index, nvidia_df["Open"], label="NVIDIA")

    btc_df = load_stock_csv("BTC-USD")
    plt.plot(btc_df.index, btc_df["Open"] / 100, "--", label="BTC/100")

    eth_df = load_stock_csv("ETH-USD")
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
