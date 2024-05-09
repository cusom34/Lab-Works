import matplotlib.pyplot as plt

t = [1.44,1.36,1,0.96,0.92,0.6,0.44,0.36,0]
r = [0,0.1,0.22,0.35,0.54,0.86,1.6,2.4,9.1] 

plt.title('Время установления колебаний')
plt.plot(r,t, marker = '.')
plt.xlabel('R, кОм')
plt.ylabel('t_уст, мс')
plt.grid()
plt.show()