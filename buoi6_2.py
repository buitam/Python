import numpy as np
import matplotlib.pyplot as plt

names, years, sales = np.loadtxt("vgsales.csv", usecols=(1,3,10), delimiter=',', skiprows=1, unpack=True, dtype=str)
vgsales = list(zip(names, years, sales))
vgsales = list(filter(lambda x: False if x[1] == 'N/A' else True, vgsales))
vgsales = sorted(vgsales, key = lambda l: l[1])
gname = input("nhap ten game trong bang: ")
game_sales = list(filter(lambda x: True if gname in x[0] else False, vgsales))
print(game_sales[0:10])

x_years= [int(row[1])for row in game_sales]
y_years=[float(row[2]) for row in game_sales]

plt.xlabel('year')
plt.ylabel('global_sales')
plt.plot(x_years,y_years, color='red')
plt.show()
