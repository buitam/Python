a = []
lhalf = int(len(a)/2)
for i in range(20):
    a.append(i)

print(a)

print("a) 1st way: ", a[:10])
print("a) 3st way: ", a[:lhalf])
print("a) 3st way: ", a[:-10])
print("a) 4st way: ", a[10:])

# n = int(input('Enter n:'))
# print('b)', a[n: -n])

n = int(input('Enter n:'))
a = a[:n]+a[-n:]
# n = int(input('Enter n:'))
# d=a.index(n)
# print(d)