
import numpy as np
from matplotlib import pyplot as plt

N = 20
X = np.arange(1, N + 1, 1)

A1 = np.random.randn(N)
A2 = np.random.randn(N)
A3 = np.random.randn(N)
# print(A1, A2, A3)
plt.scatter(X, A1, c='blue')
plt.scatter(X, A2, c='yellow')
plt.scatter(X, A3, c='green')

e1a2 = np.abs(A1 - A2)
e1a3 = np.abs(A1 - A3)
e2a3 = np.abs(A2 - A3)
f, a = plt.subplots(3, 1)
a[0].plot(X, e1a2)
a[1].plot(X, e1a3)
a[2].plot(X, e2a3)

a1a2 = np.sum(e1a2)
a1a3 = np.sum(e1a3)
a2a3 = np.sum(e2a3)
print(a1a2, a1a3, a2a3)

plt.show()
