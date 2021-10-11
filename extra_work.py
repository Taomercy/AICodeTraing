#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy
import sympy
from numpy import array, arange
import matplotlib.pyplot as plt
import statsmodels.api as sm

gdp = [22460, 11226, 34547, 4851, 5444, 2662, 4549]
consume = [7326, 4490, 11546, 2396, 2208, 1608, 2035]
data = array([gdp, consume]).T


def curve(x, k, b):
    return k*x + b


def main():
    k = sympy.Symbol('k')
    b = sympy.Symbol('b')

    def plotting(paras):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(array(data[:, 0]), array(data[:, 1]))
        x = arange(0, 50000, 50)
        y = curve(x, paras[k], paras[b])
        ax.plot(x, y, 'r')
        plt.show()

    # set y = kx + b
    loss = sympy.Symbol('loss')
    for i in data:
        loss += (i[1] - curve(i[0], k, b)) ** 2

    dlossdk = sympy.diff(loss, k)
    dlossdb = sympy.diff(loss, b)

    # 联立方程组求解
    res = sympy.solve([dlossdk, dlossdb], [k, b])
    value_k = float(res[k])
    value_b = float(res[b])
    print("线性回归方程：y={}*x+{}".format(value_k, value_b))
    # 作图
    plotting(res)

    # 显著性检验
    predicts = [i*value_k+value_b for i in gdp]
    # 回归平方和
    regression = sum((predicts-numpy.mean(consume))**2)
    print("回归平方和(RSS):", regression)
    # 残差平方和
    residual = sum((array(consume)-predicts)**2)
    print("残差平方和(ESS):", residual)
    # 总体平方和
    total = sum((consume-numpy.mean(consume))**2)
    print("总体平方和(TSS):", residual)
    # 相关系数 R^2
    r_square = 1-residual/total
    print("相关系数(R^2):", r_square)

    # when x = 5000
    value = value_k*5000 + value_b
    print("当 gdp= 5000, consume=", int(value))


if __name__ == '__main__':
    # 计算矩阵列的相关系数
    print("矩阵列的相关系数:\n", numpy.around(numpy.corrcoef(data.T), decimals=3))
    main()
