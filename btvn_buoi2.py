import numpy as np
a= np.ones((8,8))
a[1:-1, 1:-1] = 0
print("(a)",a)

b= np.ones((8,8))
b[0::2, 1::2] = 0
b[1::2, 0::2] = 0

print("(b)" , b)

c= np.random.randint(0,100,size=(8,8))
c[c%3 != 0] *= -1
print("(c)" , c)