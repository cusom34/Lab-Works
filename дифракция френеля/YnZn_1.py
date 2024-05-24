import numpy as np
import matplotlib.pyplot as plt

Yn = np.array([1.322, 1.936, 2.39, 2.78, 3.12])

Zn1 = np.array([3.16, 3.42, 3.66, 3.87, 4.02]) # a = 1313, b = 307
Zn2 = np.array([3.30, 3.57, 3.76, 3.92, 4.09]) # a = 1389, b = 231
Zn3 = np.array([3.21, 3.47, 3.63, 3.72, 3.89]) # a = 1464, b = 156

# A = np.vstack([Zn1, np.ones(len(Zn1))]).T
# k, b = np.linalg.lstsq(A, Yn, rcond = None)[0]

# def line(x):
#     lmd = 6.28*10**(-4)
#     L = 1620
#     K = np.sqrt(1313 / (307 * lmd * L))
#     b = K * np.sqrt(sum(Yn)/len(Yn)*lmd*L*307/1313)
#     return K * x - b
# x = np.linspace(Zn1[0], Zn1[-1], 100)
plt.figure(1)
plt.scatter(Zn1, Yn, color = "blue")
plt.plot(Zn1, Yn, color = "blue", label = "эксперимент")
# plt.plot(x, line(x), color = "red", label = "Теория")
plt.grid(True)
plt.legend(loc = "upper left")
plt.title("Yn(Zn); a = 1313, b = 307")
plt.xlabel("Zn")
plt.ylabel("Yn")
plt.show()