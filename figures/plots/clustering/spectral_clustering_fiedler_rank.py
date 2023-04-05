from deckz.standalones import register_plot

def main(title_plot:str, x_axis_name:str, y_axis_name:str) -> None:
    import numpy as np
    import matplotlib.pyplot as plt

    A = np.array([[0 , 1 , 1 , 1 , 0 , 0],
                [1 , 0 , 1 , 0 , 0 , 0],
                [1 , 1 , 0 , 0 , 0 , 0],
                [1 , 0 , 0 , 0 , 1 , 1],
                [0 , 0 , 0 , 1 , 0 , 1],
                [0 , 0 , 0 , 1 , 1 , 0],])
    L = np.diag(A.sum(axis=1))-A
    lbda,v = np.linalg.eigh(L)
    fiedler = np.sort(v[:,1])
    
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(np.arange(len(fiedler)),fiedler)
    ax.scatter(np.arange(len(fiedler)),fiedler)
    ax.set_title(f"{title_plot}")
    ax.set_xlabel(x_axis_name)
    ax.set_ylabel(y_axis_name)

@register_plot()
def spectral_clustering_fiedler_rank() -> None:
    main("Rang des nœuds dans le vecteur de Fiedler", "Position", "Rang")


@register_plot()
def spectral_clustering_fiedler_rank_en() -> None:
    main("Nodes rank in Fiedler vector", "Position", "Rank")
