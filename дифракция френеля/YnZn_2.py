import numpy as np
import matplotlib.pyplot as plt

Yn = np.array([1.322, 1.936, 2.39, 2.78, 3.12])

Zn1 = np.array([3.16, 3.42, 3.66, 3.87, 4.02]) # a = 1313, b = 307
Zn2 = np.array([3.30, 3.57, 3.76, 3.92, 4.09]) # a = 1389, b = 231
Zn3 = np.array([3.21, 3.47, 3.63, 3.72, 3.89]) # a = 1464, b = 156

# A = np.vstack([Zn2, np.ones(len(Zn2))]).T
# k, b = np.linalg.lstsq(A, Yn, rcond = None)[0]

# def line(x):
#     lmd = 6.71*10**(-4)
#     L = 1620
#     K = np.sqrt(1389 / (231 * lmd * L))
#     b = sum(Yn)/5 - K * sum(Zn2)/5
#     return K * x + b #- 0.18

plt.figure(1)
plt.scatter(Zn2, Yn, color = "green")
plt.plot(Zn2, Yn, color = "green", label = "эксперимент")
#plt.plot(Zn2, line(Zn2), color = "red", label = "Теория")
plt.grid(True)
plt.legend(loc = "upper left")
plt.title("Yn(Zn); a = 1389, b = 231")
plt.xlabel("Zn")
plt.ylabel("Yn")
plt.show()