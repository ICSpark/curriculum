# supervised clustering methods

# OVERVIEW:
    # perceptron: can classify linearly separable datasets
        # make_blobs
        # look at different perceptron solutions: unique? how good is a solution?
    # introduce non-linearly separable dataset
        # make swiss roll
    # SVC/nu SVC

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs, make_circles
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC, NuSVC


def dotproduct(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))

def length(v):
    return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

def manual_perceptron(X, Y, learning_rate=1, train_size=.5, n_epoch=100, bias=0, big_mode=True, plot=False):
    # initialize a random weight vector
    W = np.random.uniform(-1, 1, 2).reshape(2,1)

    if plot:
        plt.ion()

    for i in range(n_epoch):
        # calculate angle difference w/truth
        slope = W[1] / W[0]

        # plot current learning bloundary
        if plot:
            axes = plt.gca()
            if big_mode:
                axes.set_xlim(-15, 15)
                axes.set_ylim(-15, 15)
            else:
                axes.set_xlim(-1, 1)
                axes.set_ylim(-1, 1)

            x_vals = np.array(axes.get_xlim())
            y_vals = slope * x_vals
            plt.plot(x_vals, y_vals)
            plt.scatter(X[:,0], X[:,1], c=Y)
            plt.draw()
            plt.pause(0.0001)
            plt.clf()


        # split data into test, training
        X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=train_size, shuffle=True)

        # learn
        for x, y in zip(X_train, y_train):
            h = np.dot(x, W)
            yhat = -1 if h < bias else 1
            temp = learning_rate * np.dot((y - yhat), x)
            W[0] += temp[0]
            W[1] += temp[1]

        # calculate accuracy after final epoch
        Yhat = []
        for x, y in zip(X_test, y_test):
            h = np.dot(x, W)
            yhat = -1 if h < bias else 1
            Yhat.append(yhat)

        accuracy = np.mean(Yhat == Y)

    return [accuracy, slope]

# generate some data (and play around with n_samles, std, centers, center box!)
# note that centers can just be a number
X, y = make_blobs(n_samples=100, centers=[(-6, -6), (6, 6)], n_features=2, cluster_std=2.0, random_state=42)

# view it
plt.scatter(X[:,0], X[:,1], c=y)
# plt.show()

# is it linearly separable? challenge: write code to figure out whether it is
cluster_1 = X[y==0]
cluster_2 = X[y==1]
is_separable = any([cluster_1[:, k].max() < cluster_2[:, k].min() or cluster_1[:, k].min() > cluster_2[:, k].max() for k in range(2)])
print(is_separable)

# bonus challenge: use all the above to write a loop that generates gaussian datasets until one is linearly separable

# fit a perceptron to the data
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.5)
perceptron = Perceptron(fit_intercept=False)
perceptron.fit(X_train, y_train)
slope, _ = perceptron.coef_[0]

# and plot it
axes = plt.gca()
axes.set_xlim(-15, 15)
axes.set_ylim(-15, 15)
x_vals = np.array(axes.get_xlim())
y_vals = slope * x_vals
plt.plot(x_vals, y_vals)
plt.show()

# under the hood:
plt.clf()
manual_perceptron(X, y, learning_rate=.0001, plot=True)

# all of this only works for linearly separable datasets! let's see where a perceptron might fail
plt.clf()
X, y = make_circles(shuffle=True, noise=.2, factor=.5)
plt.scatter(X[:,0], X[:,1], c=y)
plt.show()

# what happens when a perceptron tries to solve this dataset?
plt.clf()
manual_perceptron(X, y, big_mode=False, plot=True)

# the perceptron is sad and confused :(

# more complicated algorithms to the rescue! use algorithms whose decision boundaries aren't linear
# the idea behind support vector machines is "soft" classification, as opposed to the perceptron's "hard" classification
# balance between wanting to make the gap between clusters as large as possible, and wanting as few misclassifications as possible
# control this with C: small C = small gap and few misclassifications, large C = large gap and more misclassifications

xx, yy = np.meshgrid(np.linspace(-1, 1, 500),
                     np.linspace(-1, 1, 500))


C_vals = [.001, .01, .1, 1, 10]
for C in C_vals: 
    svc = SVC(C=C, random_state=42)
    svc.fit(X, y)

    # plot the decision function for each datapoint on the grid
    Z = svc.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)


    plt.contour(xx, yy, Z, levels=[0], colors='k', linewidths=2,linestyles='solid')
    plt.scatter(X[:,0], X[:,1], s=25, c=y, cmap=plt.cm.Paired,
                edgecolors='b')
    plt.xticks(())
    plt.yticks(())
    plt.title(r'Decision boundary of $C$-SVC (C = {})'.format(C))
    plt.axis([-1.5, 1.5, -1.5, 1.5])
    plt.show()

# nu svc is the same idea, but instead of having a ratio of how wide the boundary is, nu controls the fraction of misclassified points
nu_vals = [.2, .4, .6, .8, .99]
for nu in nu_vals: 
    nu_svc = NuSVC(nu=nu, random_state=42)
    nu_svc.fit(X, y)

    # plot the decision function for each datapoint on the grid
    Z = nu_svc.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)


    plt.contour(xx, yy, Z, levels=[0], colors='k', linewidths=2,linestyles='solid')
    plt.scatter(X[:,0], X[:,1], s=25, c=y, cmap=plt.cm.Paired,
                edgecolors='b')
    plt.xticks(())
    plt.yticks(())
    plt.title(r'Decision boundary of $\nu$-SVC ($\nu$ = {})'.format(nu))
    plt.axis([-1.5, 1.5, -1.5, 1.5])
    plt.show()