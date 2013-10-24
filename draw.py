import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.cm as cm
from reset import reset_plots

def boxes(img,rects):
    reset_plots()
    for r in rects:
        minr, minc, maxr, maxc = r
        fig, ax = plt.subplots(ncols=1, nrows=1)
        ax.imshow(img,cmap = cm.Greys_r)
        ax.add_patch(mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                        fill=False, edgecolor='red', linewidth=2))
        fig.show()
