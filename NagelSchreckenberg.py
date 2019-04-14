#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def clip(x, path):
    for i in range(len(x)):
        if x[i] > path:
            x[i] %= path


def main():
    path = 5000   # 环形公路长度
    n = 100       # 公路中的车辆数目
    v0 = 5        # 车辆的初始速度
    p = 0.3       # 随机减速概率
    times = 3000  # 模拟时间

    np.random.seed(0)
    x = np.random.rand(n) * path            # 所有车辆在环形公路上的随机位置
    x.sort()
    v = np.tile([v0], n).astype(np.float)   # 所有车辆的初速度向量
    plt.figure(figsize=(10, 8), facecolor='w')

    for t in range(times):
        plt.scatter(x, [t] * n, s=1, c='k', alpha=0.05)
        for i in range(n):
            if x[(i+1) % n] > x[i]:
                d = x[(i+1) % n] - x[i]
            else:
                d = path - x[i] + x[(i+1) % n]
            if v[i] < d:
                if np.random.rand() > p:
                    v[i] += 1
                else:
                    v[i] -= 1
            else:
                v[i] = d - 1
        v = v.clip(0, 150)
        x += v
        clip(x, path)

    plt.xlim(0, path)
    plt.ylim(0, times)
    plt.xlabel('x', fontsize=16)
    plt.ylabel('times', fontsize=16)
    plt.title('Nagel Schreckenberg', fontsize=16)
    plt.tight_layout(pad=2)
    plt.show()


if __name__ == '__main__':
    main()
