import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
from sklearn import datasets

def plot_prediction(X, Y, predict_func, params):
    X = np.array(X)
    Y = np.array(Y)
    plt.figure(figsize=(10, 6))
    plt.scatter(X[Y == 0][:, 0], X[Y == 0][:, 1], color='b', label='0')
    plt.scatter(X[Y == 1][:, 0], X[Y == 1][:, 1], color='r', label='1')
    plt.legend()
    x1_min, x1_max = X[:,0].min(), X[:,0].max(),
    x2_min, x2_max = X[:,1].min(), X[:,1].max(),
    xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
    grid = np.c_[xx1.ravel(), xx2.ravel()]
    probs = predict_func(params['w'], params['b'], grid.T).reshape(xx1.shape)
    plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors='black')