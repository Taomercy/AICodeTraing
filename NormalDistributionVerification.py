#!/usr/bin/env python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy


def main():
    #一次均匀分布
    u = numpy.random.uniform(0.0, 1.0, 10000)
    plt.hist(u, 80, facecolor='b', alpha=0.75)
    plt.grid(True)
    plt.show()

    #累计10000次均匀分布，得到正态分布
    times = 10000
    for time in range(times):
        u += numpy.random.uniform(0.0, 1.0, 10000)

    print len(u)
    u /= times
    plt.hist(u, 80, facecolor='b', alpha=0.75)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()

