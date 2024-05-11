import matplotlib.pyplot as plt
import openpyxl
from scipy.interpolate import PchipInterpolator
import numpy as np

r = 1500 +250 + 365
l = 0.39
c = 5.7e-9
E0= 0.248

def UR_func(f):
       return  E0*r/(r**2 + (2*np.pi*f*l-1/(2*np.pi*f*c))**2)**0.5

def UC_func(f):
    return E0/(2*np.pi*f*c*(r**2 + (2*np.pi*f*l-1/(2*np.pi*f*c))**2)**0.5)

def UL_func(f):
       return  E0*2*np.pi*f*l/((r**2 + (2*np.pi*f*l-1/(2*np.pi*f*c))**2)**0.5)

path = "R1500_Om.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

data = []
for i in range(1,4+1):
    for j in range(2,51+1):
        data +=[sheet_obj.cell(j, i).value]

freq = range(0,6500)
f = data[:50]
UC = data[50:100]
UL = data[100:150]
UR = data[150:200]

UR_new = [UR_func(elem) for elem in freq[1:]]
UC_new = [UC_func(elem) for elem in freq[1:]]
UL_new = [UL_func(elem) for elem in freq[1:]]

fig = plt.figure(figsize=(15, 4))
plt.title('R = 1500 Ом')

plt.scatter(f,UC, marker = '.', label='UC')
UC_inter = PchipInterpolator(f, UC)
#plt.plot(freq,UC_inter(freq)+0.005)
plt.plot(freq[1:],UC_new)

plt.scatter(f,UL, marker = '.', label='UL')
UL_inter = PchipInterpolator(f, UL)
#plt.plot(freq,UL_inter(freq)+0.005)
plt.plot(freq[1:],UL_new)

plt.scatter(f,UR, marker = '.', label='UR')
UR_inter = PchipInterpolator(f, UR)
#plt.plot(freq,UR_inter(freq) + 0.015)
plt.plot(freq[1:],UR_new)

plt.legend(loc='upper right')
plt.ylabel("U, В")
plt.xlabel("f, Гц")
plt.xticks(range(0,6501,250))
plt.grid()
plt.show()
