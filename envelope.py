from mpl_toolkits.axes_grid.axislines import SubplotZero
from matplotlib.transforms import BlendedGenericTransform
import matplotlib.pyplot as plt
import numpy as np

def f(x, t):
    return t * x - t**2  # 関数fの定義

if 1:
    fig = plt.figure(1)
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)

    ax.axhline(linewidth=1.7, color="black")
    ax.axvline(linewidth=1.7, color="black")

    plt.xticks([])
    plt.yticks([])
    plt.ylim([-20,40])

    ax.text(0, 1.05, '$y$', transform=BlendedGenericTransform(ax.transData, ax.transAxes), ha='center')
    ax.text(1.05, 0, '$x$', transform=BlendedGenericTransform(ax.transAxes, ax.transData), va='center')
    # 軸の書式設定(謎)

    for direction in ["xzero", "yzero"]:
        ax.axis[direction].set_axisline_style("-|>")
        ax.axis[direction].set_visible(True)

    for direction in ["left", "right", "bottom", "top"]:
        ax.axis[direction].set_visible(False)

    x = np.linspace(-10, 10, 200)
    for i in range(-5,6):  # グラフを書く作業を繰り返す範囲
        y = f(x, t=i)
        ax.plot(x, y, 'black', linewidth=2)
    plt.show()