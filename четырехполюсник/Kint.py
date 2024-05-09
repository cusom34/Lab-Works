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

#теоретический коэф. усиления
x = numpy.arange(0, 3001, 50)
y =1/((2*10**(-2)*math.pi *x)**2 + 1)**0.5
plt.plot(x, y, marker='o', label='Теория')

#практический коэф. усиления
a = numpy.array([20,40,60,80,100,150,200,300,400,500,1000,2000,3000])
b = numpy.array([5.04/16.4, 8/16.4, 6.48/16.4,5.28/16,4.48/16.4,3.2/16.6,2.48/16.4,1.76/16.6,1.28/16.6,1.02/16.4,
                 0.512/16.4,0.272/16.4,0.176/16.4 ])
print (b)
plt.plot(a, b, marker='^', label='Практика')

plt.xticks(numpy.arange(0,3001,100))
plt.grid(color = 'black')
plt.title('Коэф-т передачи интегрирующего четырехполюсника')
plt.legend(loc='upper right')
plt.xlabel('w/2pi')
plt.ylabel('K(w/2pi)')
plt.show()
#дз поставить anaconda navigator и нарисовать что-нибудь