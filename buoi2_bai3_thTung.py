import numpy as np
y = np.array([0., 1.3, 5. , 10.9, 18.9, 28.7, 40.])
t = np.array([0., 0.49, 1. , 1.5 , 2.08, 2.55, 3.2])

v = (y[1:]-y[:-1])/(t[1:]-t[:-1])
print(v)