#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy
import sympy
from numpy import array, arange
import matplotlib.pyplot as plt
import statsmodels.api as sm

gdp = [22460, 11226, 34547, 4851, 5444, 2662, 4549]
consume = [7326, 4490, 11546, 2396, 2208, 1608, 2035]
x = [0.00027, 0.00024, 0.00021, 0.00019, 0.00016, 0.00013, 0.00011, 0.00008, 0.00005, 0.00003]
y = [3.2771, 3.101, 2.8127, 2.5224, 2.3108, 2.067, 1.7388, 1.5044, 1.1264, 0.5129]
data = array([gdp, consume]).T
# data = array([x, y]).T


def curve(x, k, b):
    return k*x + b


def verfiy(k, b, data):
    data_x = data[:, 0]
    data_y = data[:, 1]
    # 显著性检验
    predicts = [i*k+b for i in data_x]
    # 回归平方和
    regression = sum((predicts-numpy.mean(data_y))**2)
    print("回归平方和(RSS):", regression)
    # 残差平方和
    residual = sum((array(data_y)-predicts)**2)
    print("残差平方和(ESS):", residual)
    # 总体平方和
    total = sum((data_y-numpy.mean(data_y))**2)
    print("总体平方和(TSS=RSS+ESS):", total)
    # 相关系数 R^2
    r_square = 1-residual/total
    print("相关系数(R^2):", r_square)
    return r_square


def main():
    k = sympy.Symbol('k')
    b = sympy.Symbol('b')

    def plotting(paras):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(array(data[:, 0]), array(data[:, 1]))
        max_number = data[:, 0].max()
        min_number = data[:, 0].min()
        step = (max_number - min_number) / 1000
        x = arange(min_number * 0.1, max_number * 1.1, step)
        y = curve(x, paras[k], paras[b])
        # plt.gca().invert_xaxis() #坐标轴逆序
        plt.title("formula: y={}*x+{}\nR^2={}".format(value_k, value_b, r_square))
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
    # 验证
    r_square = verfiy(value_k, value_b, data)
    # 作图
    plotting(res)


if __name__ == '__main__':
    # 计算矩阵列的相关系数
    print("矩阵列的相关系数:\n", numpy.around(numpy.corrcoef(data.T), decimals=3))
    main()
