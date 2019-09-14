def inverse(*numbers):
    print("gốc:" , numbers)
    print("Đảo chuỗi: ", end="")
    for n in numbers:
        n=1/n
    print(n, end="")
     #print(numbers) * là cho phép nhập vào nhiều tham số, nhưng các tham số đó dạng tuple

print(inverse(2))