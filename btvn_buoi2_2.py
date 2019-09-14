
import numpy as np
distionary={"tam":7,"Tham":5, "hoa":8}
distionary["mai"]=7.3
print(distionary)
b=max(distionary.values())
print(b)
#-----------------------Tính Max
d=max(distionary)
print(d)
#------------------------Tính Min
c=min(distionary.values())
print(c)
#-----------------------Tính trung bình
print(np.mean(list(distionary.values())))
#-----------------------Xóa
distionary.pop("hoa")
print(distionary)
