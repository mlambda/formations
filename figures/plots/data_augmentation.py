from deckz.standalones import register_plot


def _work(
    original_label: str,
    rotation_label: str,
    translation_label: str,
    homothety_label: str,
    shear_label: str,
) -> None:
    import matplotlib.pyplot as plt
    from matplotlib.axes import Axes
    from numpy import array, concatenate, load, ndarray, zeros
    from PIL import Image

    from .utils import resource_as_binary_tempfile

    with resource_as_binary_tempfile("mnist-3.npz") as fh:
        x = load(fh)["x"]

    x /= 255.0

    def showball(ax: Axes, img: ndarray, title: str) -> None:
        ax.imshow(img, cmap="gray_r")
        ax.set_title(title, fontsize=20)
        ax.axis("off")

    f, ax = plt.subplots(1, 5, figsize=(15, 3))

    def whitegrid() -> ndarray:
        return zeros((80, 80))

    def whitegrid2(x: ndarray) -> ndarray:
        m = whitegrid()
        m[1::7, :] = 0.1
        m[:, 1::7] = 0.1
        return x + m

    augm = whitegrid()

    augm[27:55, 27:55] = x
    showball(ax[0], whitegrid2(augm), original_label)

    image = Image.fromarray(x)
    image = image.rotate(20)
    augm = whitegrid()
    augm[27:55, 27:55] = array(image)
    showball(ax[1], whitegrid2(augm), rotation_label)

    augm = whitegrid()
    augm[12:40, 50:78] = x
    showball(ax[2], whitegrid2(augm), translation_label)

    image = Image.fromarray(x)
    image = array(image.resize((80, 80)))
    image[image < 0.1] = 0
    showball(ax[3], whitegrid2(image), homothety_label)

    def circus(x: ndarray, k: int) -> ndarray:
        decalage = int(14 * ((k - 14) / 14) ** 2)
        return concatenate((x[decalage:], x[:decalage]), axis=None)

    shear = x
    for k in range(28):
        shear[k, :] = circus(shear[k, :], k)
    augm = whitegrid()
    augm[27:55, 27:55] = shear
    showball(ax[4], whitegrid2(augm), shear_label)


@register_plot()
def data_augmentation() -> None:
    _work(
        original_label="Originale",
        rotation_label="Rotation",
        translation_label="Translation",
        homothety_label="Homothétie",
        shear_label="Déformation",
    )


@register_plot()
def data_augmentation_en() -> None:
    _work(
        original_label="Original",
        rotation_label="Rotation",
        translation_label="Translation",
        homothety_label="Homothety",
        shear_label="Shear",
    )
