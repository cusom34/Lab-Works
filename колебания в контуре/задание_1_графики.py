import matplotlib.pyplot as plt

R = [0,0.1,0.22,0.35,0.54,0.86, 1.6, 2.4]
T= []
T += [300 for i in range(len(R))]
d = [1.08, 1.1,1.16, 1.225, 1.32, 1.48, 2, 2.73]

fig = plt.figure(figsize=(10, 4))

plt.subplot(1,2,1)
plt.title('Периоод собственных колебаний')
plt.plot(R,T, marker = '.')
plt.ylabel("T, мкс")
plt.xlabel("R, кОм")
plt.grid()

plt.subplot(1,2,2)
plt.title('Декремент затухания')
plt.plot(R,d, marker = '.')
plt.ylabel("d")
plt.xlabel("R, кОм")
plt.grid()

plt.show()
