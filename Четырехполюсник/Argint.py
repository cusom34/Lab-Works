import math
import numpy #модуль с массивами и мат. ф-ми
import matplotlib.pyplot as plt #плотит графики

"""
a = numpy.zeros([2,3]) #двумерный массив с нулями
b = numpy.ones([2,3])  #двумерный массив с единицами

print(a)

c = numpy.arange(0,10,0.1) #одномерный массив заполняемый по диапазону
print(c)
"""

#теоретическая фаза
x = numpy.arange(0, 3001, 50)
y = numpy.arctan(-2*10**(-2)*math.pi*x)
plt.plot(x, y, marker='o', label='Теория')

#практическая фаза
a = numpy.array([20,40,60,80,100,150,200,300,400,500,1000,2000,3000])
b = -numpy.arcsin(numpy.array([6.6/16.4, 10.2/16.4, 12.6/16.4, 13.4/16, 14.4/16.4, 15.2/16.6, 15.4/16.4, 16.6/16.6,
                              16.6/16.6, 16.4/16.4, 16.4/16.4, 16.4/16.4, 16.4/16.4]))
print (b)
plt.plot(a, b, marker='^', label='Практика')

plt.xticks(numpy.arange(0,3001,100))
plt.grid(color = 'black')
plt.title('Фазовая хар-ка интегрирующего четырехполюсника')
plt.legend(loc='upper right')
plt.xlabel('w/2pi')
plt.ylabel('Arg(w/2pi)')
plt.show()
#дз поставить anaconda navigator и нарисовать что-нибудь