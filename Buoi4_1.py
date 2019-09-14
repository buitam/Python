#Having a list of random integers (100 elements)
#b) Find negative numbers and make them positive with the same absolute value
#c) Extract prime numbers from the list above. Print result (you may need to write a prime function)
#d) For each prime number, print the numbers in the list which is divisible by that prime

import numpy as np
mlist = list(np.random.randint(-100,100,size = 100))
print("List:", mlist)
mlist = list(map(lambda x: -x if x < 0 else x, mlist))
# x = -x, x = x.
print("Positive list:",mlist)
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
print("Primes", list(filter(is_prime, list(filter(is_prime,range(0,100))))))  
primes = sorted(list(set(filter(is_prime,mlist))))
print("Primes in my_list: ", primes)
#  filter : Hàm lọc
#d:
def divisible_prime():
    for p in primes:
        print("[{0}] :".format(p), end='')
        for i in mlist: 
            if i %p ==0:
                print("{0}".format(i), end=' ')
        print("\n")


divisible_prime()