b=[]

while len(b)<5:
    a=[]
    for i in range(5):
        a.append(i)
    b.append(a)

print("Mảng b: ",b)
print("3 rows giữa: ", b[1:-1])
print("2 rows cuối: ", b[3:])
print("2 rows cuối: ", b[3:])
print("2 rows cuối: ", b[-2:])

n = int(input('Enter n:'))
c = b[n]
print(c)
print("max: ", max(c))
print("max: ", min(c))
