import numpy as np
mylist = np.random.randint(100,size=20)
print(mylist)
#-------------
for i in mylist:
    if i>50:
        print(i)

#---------b
c=[]
for i in mylist:
    if i>np.mean(list(mylist)):
        c.append(i)
        print("b: ", i)
        print("b: ", c)

#---------c
d=[]
for i in c:
    if i % 2 == 0:
        d.append(i)
        print("c", i)
        print("d", d)
#_--------d
#grt50=[mylist[i] for i in range(20) if mylist[i]>50]
#PRINT(GRT50)