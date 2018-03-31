import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from matplotlib import cm

cmap = cm.get_cmap('gnuplot')


def scatter_matrix_plot():
    scatter = scatter_matrix(X_train, c=y_train, marker='o', s=40, hist_kwds={'bins': 15}, figsize=(9, 9), cmap=cmap)


def scatter_3d_plot():
    # plotting a 3D scatter plot
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X_train['width'], X_train['height'], X_train['color_score'], c=y_train, marker='o', s=100)
    ax.set_xlabel('width')
    ax.set_ylabel('height')
    ax.set_zlabel('color_score')
    plt.show()


if __name__ == "__main__":
    scatter_plot()
