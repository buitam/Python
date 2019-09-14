import numpy as np
import matplotlib.pyplot as plt
# BÀI 1 
#x = np.arange(-1,3,0.1)
#y = 3*x*x
#plt.plot(x,y)
#plt.show()

#bai 2
x = np.arange(-15,15,0.1)
y = np.cos(x)/(1+(1/5)*x*x)
plt.plot(x,y, 'grey', label = 'theory')# đổi màu đường biểu đồ
plt.xlabel('x')
plt.ylabel('transverse displacement')
plt.axhline(color = 'grey', zorder = -1)
plt.axhline(color = 'blue', zorder = -1)
plt.show()