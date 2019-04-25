#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()


def meanX(dataX):
    return np.mean(dataX, axis=0)


def pca(XMat, k):
    average = meanX(XMat)
    m, n = np.shape(XMat)
    data_adjust = []
    avgs = np.tile(average, (m, 1))
    data_adjust = XMat - avgs
    covX = np.cov(data_adjust.T)
    featValue, featVec = np.linalg.eig(covX)
    index = np.argsort(-featValue)
    finalData = []
    if k > n:
        print "k must lower than feature number"
        return
    else:
        selectVec = np.matrix(featVec.T[index[:k]])
        finalData = data_adjust * selectVec.T
        reconData = (finalData * selectVec) + average
    return finalData, reconData


def plotBestFit(data1, data2):
    dataArr1 = np.array(data1)
    dataArr2 = np.array(data2)

    m = np.shape(dataArr1)[0]
    axis_x1 = []
    axis_y1 = []
    axis_x2 = []
    axis_y2 = []
    for i in range(m):
        axis_x1.append(dataArr1[i, 0])
        axis_y1.append(dataArr1[i, 1])
        axis_x2.append(dataArr2[i, 0])
        axis_y2.append(dataArr2[i, 1])
    # ax = fig.add_subplot(111)
    ax = fig.add_subplot(122)
    ax.scatter(axis_x1, axis_y1, s=50, c='red', marker='s')
    ax.scatter(axis_x2, axis_y2, s=50, c='blue')
    plt.xlabel('x1')
    plt.ylabel('x2')


def loaddata(datafile):
    return np.array(pd.read_csv(datafile, sep=" ", header=-1)).astype(np.float)


def main():
    datafile = "pca_data.txt"
    XMat = loaddata(datafile)
    k = 2
    return pca(XMat, k)


def test():
    X = [[2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2, 1, 1.5, 1.1],
         [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9]]
    XMat = np.matrix(X).T
    k = 2
    ax = fig.add_subplot(121)
    plt.scatter(X[0], X[1], c='g', marker='x')
    return pca(XMat, k)


if __name__ == "__main__":
    finalData, reconMat = test()
    plotBestFit(finalData, reconMat)
    plt.show()