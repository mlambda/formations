from deckz.standalones import register_plot


def main(drivers_label: str, cnns_label: str) -> None:
    from io import StringIO
    from pkgutil import get_data

    import matplotlib.pyplot as plt
    from pandas import DataFrame, read_csv

    nvidia_path = "data/stock-prices/NVDA.csv"
    btc_path = "data/stock-prices/BTC-USD.csv"
    eth_path = "data/stock-prices/ETH-USD.csv"

    def tonum(x):
        return int(x[0:4]) + (int(x[5:7]) - 1) * 30 / 365 + int(x[9:]) / 365

    def convert(df):
        return df.apply(lambda x: tonum(x))

    def load_csv(path: str) -> DataFrame:
        content = get_data(__name__, path)
        if content is None:
            raise RuntimeError(f"Could not load {path}")
        return read_csv(StringIO(content.decode("utf8")))

    nvidia_df = load_csv(nvidia_path)
    x = nvidia_df["Date"]
    y = nvidia_df["Open"]
    x_nvidia = convert(x)
    plt.plot(x_nvidia, y, label="NVIDIA")

    btc_df = load_csv(btc_path)
    x = btc_df["Date"]
    y = btc_df["Open"]
    x_btc = convert(x)
    plt.plot(x_btc, y / 100, label="BTC/100")

    eth_df = load_csv(eth_path)
    x = eth_df["Date"]
    y = eth_df["Open"]
    x_eth = convert(x)
    plt.plot(x_eth, y / 10, label="ETH/10")

    cuda = tonum("2007-06-23")
    cuda = [cuda, cuda]
    catneuron = tonum("2012-07-12")
    catneuron = [catneuron, catneuron]
    plt.plot(cuda, [0, 100], c="k")
    plt.annotate(drivers_label, (cuda[0] - 2.2, 115))
    plt.plot(catneuron, [0, 200], c="k")
    plt.annotate(cnns_label, (catneuron[0] - 2.2, 215))
    plt.legend(prop={"size": 15})


@register_plot()
def nvidia_stock_history() -> None:
    main(drivers_label="Drivers CUDA", cnns_label="CNNs performants")


@register_plot()
def nvidia_stock_history_en() -> None:
    main(drivers_label="CUDA drivers", cnns_label="Efficient CNNs")
