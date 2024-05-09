import matplotlib.pyplot as plt
import openpyxl
from scipy.interpolate import PchipInterpolator

path = "R100_Om.xlsx"
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

fig = plt.figure(figsize=(15, 4))
plt.title('R = 100 Ом')

plt.scatter(f,UC, marker = '.', label='UC')
UC_inter = PchipInterpolator(f, UC)
plt.plot(freq,UC_inter(freq)+ 0.05)

plt.scatter(f,UL, marker = '.', label='UL')
UL_inter = PchipInterpolator(f, UL)
plt.plot(freq,UL_inter(freq)+ 0.05)

plt.scatter(f,UR, marker = '.', label='UR')
UR_inter = PchipInterpolator(f, UR)
plt.plot(freq,UR_inter(freq) + 0.05)

plt.legend(loc='upper right')
plt.ylabel("U, В")
plt.xlabel("f, Гц")
plt.xticks(range(0,6501,250))
plt.grid()
plt.show()
