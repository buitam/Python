import numpy as np
import math
np.seterr(divide='ignore', invalid='ignore')
x = np.arange(1,10,2)
result = []
n = int(input('Enter n:'))
for i in range(len(x)): 
    if n == 0:
        th0 = (math.sin(x[i])) / (x[i])
        result.append(th0) 
        i += 1
    elif n == 1:
        th1 =  (math.sin(x[i])/(x[i]*x[i]) ) - math.cos(x[i])/x[i]
        result.append(th1) 
        i += 1
    elif n==2:
        th2 =  ((3/(x[i]*x[i]) - 1)*(math.sin(x[i])/x[i]) ) - (3*math.cos(x[i])/ (x[i]*x[i]))
        result.append(th2) 
        i += 1
print(result)

