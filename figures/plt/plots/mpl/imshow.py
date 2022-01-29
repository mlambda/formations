from deckz.standalones import register_plot


def main(contour=False,cumul=False):
    import matplotlib.pyplot as plt
    import numpy as np
    
    # make data
    X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
    Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
    if contour:
        plt.contour(X,Y,Z)
    elif not cumul:
        plt.imshow(Z)
    else :
        fig,ax=plt.subplots()
        X=(X/6+0.5)*256
        Y=(Y/6+0.5)*256
        
        ax.imshow(Z)
        ax.contour(X,Y,Z,cmap='plasma')

@register_plot()
def imshow():
    main(contour=False)

@register_plot()
def contour():
    main(contour=True)


