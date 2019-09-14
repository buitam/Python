import numpy as np
ten = np.array(["tam", "tham", "duy", "", "nguyen"])
tuoi = np.array([-20, 15, 60, 190, 88])
ten[ten==""] = "John"
print(ten)

d =max(tuoi)
print(d)

e =min(tuoi)
print(e)

maxten = max(ten, key=len)
print('ten: ',maxten)
print('longest name size: ', max(list(map(len,ten))))

minten = min(ten, key=len)
print('ten: ', minten)
print('shortest name size: ', min(list(map(len,ten))))