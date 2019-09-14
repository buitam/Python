import numpy as np
a = np.linspace(0, 20, num=10, dtype=int, endpoint=False)
print(a)

b = np.arange(0,20,20/10, dtype=int)
print(b)

c = np.random.randint(0,100,20,dtype=int)
print(c)

d = c[c%2==0]
d.sort()
print(d)

f = c[c%2!=0]
f.sort()
print(f)

e = np.concatenate([f, d])
print(e)
