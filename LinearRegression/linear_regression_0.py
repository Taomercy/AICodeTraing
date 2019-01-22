#!/usr/bin/env python
# -*- coding:utf-8 -*-
from numpy import *
import matplotlib.pylab as plt
import sympy
import time

'''
data = array([
    [1.2, 3.6],
    [2.3, 4.6],
    [1.8, 7.6],
    [5.4, 15.8],
])
'''

def plotting(data, k, b):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(array(data[:, 0]), array(data[:, 1]))
    x = arange(0, 10, 0.01)
    y = curve(x, k, b)
    ax.plot(x, y, 'r')
    plt.show()


def curve(x, k, b):
    return k*x + b


def main():
    start = time.time()

    # set y = kx + b
    data = loadtxt('data.csv', delimiter=',')
    k = sympy.Symbol('k')
    b = sympy.Symbol('b')
    loss = sympy.Symbol('loss')
    for i in data:
        loss += (i[1] - (k*i[0] + b))**2
    
    dlossdk = sympy.diff(loss, k)
    dlossdb = sympy.diff(loss, b)
    
    # 对k求偏导数
    print "dlossdk:", dlossdk
    # 对b求偏导数
    print "dlossdb:", dlossdb
    
    # 联立方程组求解
    res = sympy.solve([dlossdk, dlossdb], [k, b])
    print "k =", res[k]
    print "v =", res[b]
    # 作图
    end = time.time()
    print "use time:", end -start

    plotting(data, res[k], res[b])


if __name__ == '__main__':
    main()
