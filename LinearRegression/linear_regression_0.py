#!/usr/bin/env python
# -*- coding:utf-8 -*-
from numpy import *
import matplotlib.pylab as plt
import sympy

data = array([
    [1.2, 3.6],
    [2.3, 4.6],
    [1.8, 7.6],
    [5.4, 15.8],
])

#data = loadtxt('data.csv', delimiter=',')


def curve1(x, k, b):
    return k*x + b


def main1():
    k = sympy.Symbol('k')
    b = sympy.Symbol('b')

    def plotting(paras):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(array(data[:, 0]), array(data[:, 1]))
        x = arange(0, 10, 0.01)
        y = curve1(x, paras[k], paras[b])
        ax.plot(x, y, 'r')
        plt.show()

    # set y = kx + b
    loss = sympy.Symbol('loss')
    for i in data:
        loss += (i[1] - curve1(i[0], k, b)) ** 2

    dlossdk = sympy.diff(loss, k)
    dlossdb = sympy.diff(loss, b)

    # 对k求偏导数
    print("dlossdk:", dlossdk)
    # 对b求偏导数
    print("dlossdb:", dlossdb)

    # 联立方程组求解
    res = sympy.solve([dlossdk, dlossdb], [k, b])
    print("k =", res[k])
    print("v =", res[b])
    # 作图
    plotting(res)


def curve2(x, a, b, c):
    return a*x**2 + b*x + c


def main2():
    a, b, c = sympy.symbols('a b c')
    
    def plotting(paras):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(array(data[:, 0]), array(data[:, 1]))
        x = arange(0, 10, 0.01)
        y = curve2(x, paras[a], paras[b], paras[c])
        ax.plot(x, y, 'r')
        plt.show()

    # set y = ax**2 + kx +b
    loss = sympy.Symbol('loss')
    for i in data:
        loss += (i[1] - curve2(i[0], a, b, c))**2
    
    dlossda = sympy.diff(loss, a)
    dlossdb = sympy.diff(loss, b)
    dlossdc = sympy.diff(loss, c)
    
    print("dlossda:", dlossda)
    print("dlossdb:", dlossdb)
    print("dlossdc:", dlossdc)
    
    # 联立方程组求解
    res = sympy.solve([dlossda, dlossdb, dlossdc], [a, b, c])
    print("a =", res[a])
    print("b =", res[b])
    print("c =", res[c])
    # 作图
    plotting(res)


if __name__ == '__main__':
    main1()
    main2()

