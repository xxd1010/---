

import numpy as np
from matplotlib import pyplot as plt

# 获取坐标轴
ax = plt.gca()
# 将上方边框颜色设置为无色
ax.spines['top'].set_color('none')
# 将右方边框颜色设置为无色
ax.spines['right'].set_color('none')
#
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))


class draw():
    def __init__(self, n, N, step):
        super().__init__()
        self.n = n
        self.N = N
        self.step = step
        self.main()

    def add_point(self, x, y, s=20, c='b', m='.'):
        plt.scatter(x, y, s, c, m)

    def main(self):
        plt.draw()


n = 3
N = 4
step = 0.1

# 三角函数变量控制
A = 1
omiga = 1
theta = np.pi / 4 * 0
bs = omiga * np.random.random(1) * 0
bt = omiga * np.random.random(1)

xs = np.arange(-N, N, step)
# ys = xs ** n
ys = A * np.cos(omiga * xs + theta) + bs
# 绘制数据散点图
plt.scatter(xs, ys, s=5, c='r', marker='^')

xt = 2 * N * np.random.random(1) - N
# yt = xt ** n + 2 * xt * np.random.random(1) - xt
yt = A * np.cos(omiga * xt + theta) + bt
# 绘制目标点
plt.scatter(xt, yt, s=50)

l = len(xs)
e = np.zeros(l)
for i in range(l):
    # 计算误差
    xs_s = xs[i] % omiga
    xt_t = xt % omiga
    # print(xs_s, xt_t)
    if ys[i] > 0:
        e[i] = np.sqrt((xs_s - xt_t) ** 2 + (ys[i] - yt) ** 2)
    else:
        e[i] = np.sqrt((xs_s - xt_t) ** 2 + (ys[i] - yt) ** 2)
    # print(e[i])

# 绘制误差散点图
plt.scatter(xs, e, s=5, c='b', marker='v')

plt.show()





