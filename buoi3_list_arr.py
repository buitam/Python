import numpy as np
s="tam"
v= 6.7
l = ['vatly', 'hoahoc', 1997, 2000]
a= [1, 3.5, "Hello"]

def test(s,v,l,a):
    s="tôi tên"
    v= np.pi**2
    l[-1] = 'end'
    a[0] = 98.2
    return s,v,l,a
    
print("danh sách 1: ", test(s,v,l,a))
print("danh sách 2: ",s,v,l,a)