#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys


def statistic(number):
    number -= int(number)
    print "number=", int(10 ** number) - 1
    frequency[int(10 ** number) - 1] += 1


if __name__ == '__main__':
    N = int(sys.argv[1])
    x = range(1, N + 1)
    frequency = np.zeros(9, dtype=np.int)
    f = 1

    y = np.cumsum(np.log10(x))
    map(statistic, y)

    plt.figure(facecolor='w')
    t = np.arange(1, 10)
    plt.plot(t, frequency, 'b-', t, frequency, 'go', lw=2, markersize=8)
    for x, y in enumerate(frequency):
        plt.text(x + 1.1, y, frequency[x], verticalalignment='top', fontsize=15)

    plt.title('%d! Frequency of occurrence of first digit' % N, fontsize=18)
    plt.xlim(0.5, 9.5)
    plt.ylim(0, max(frequency) * 1.03)
    plt.grid(True)
    plt.show()
