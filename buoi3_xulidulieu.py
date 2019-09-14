import numpy as np
a = np.array([1.e-6, -1.e-7, 3., 100., 3.e+6, 2019.])
np.set_printoptions(precision=5)

def xuli(values,dulieunho,dulieubig):
    dulieubig(values)
    dulieunho(values)

def convertToZero(values):
    values[np.abs(values)<1.e-5] = 0

def tenTimes(values):
    values[np.abs(values)<1.e-5] *= 10

def half(values):
    values[np.abs(values)>1.e+5] /= 2

def square(values):
    values[np.abs(values)>1.e+5] **= 0.5
print("Dữ liệu gốc: ", a)

xuli(a,tenTimes,half)
print("Dữ liệu 1: ", a)

xuli(a,convertToZero,square)
print("Dữ liệu 2: ", a)

