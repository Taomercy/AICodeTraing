#!/usr/bin/python
# coding:utf8
# 矩阵求解
from numpy import *
import matplotlib.pylab as plt


def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1               
    dataMat = []
    labelMat = []
    with open(fileName) as fr:
        for line in fr.readlines():
            lineArr =[]
            curLine = line.strip().split('\t')
            for i in range(numFeat):
                lineArr.append(float(curLine[i]))
            dataMat.append(lineArr)
            labelMat.append(float(curLine[-1]))

    return dataMat, labelMat


def standRegres(xArray, yArray):

    xMatix = mat(xArray)
    yMatix = mat(yArray).T

    #xTx: 矩阵行列式
    xTx = xMatix.T*xMatix

    # 如果矩阵行列式为0， 则没有逆矩阵
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return

    # 矩阵求解
    #ws = xTx.I * (xMatix.T*yMatix)
    ws = xMatix.I * yMatix
    return ws


def regression():
    xArray, yArray = loadDataSet("data.txt")
    xMatix = mat(xArray)
    yMatix = mat(yArray)
    ws = standRegres(xArray, yArray)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(array(xMatix[:, 1]), array(yMatix.T[:, 0]))
    xCopy = xMatix.copy()
    xCopy.sort(0)
    yHat = xCopy * ws
    ax.plot(xCopy[:, 1], yHat)
    plt.show()


if __name__ =='__main__':
    regression()
