import numpy as np
a = np.array([['john', '10:40',4],
['haha', '10:40',3],
['lala', '10:40',6]])
nppizza = (row[2] for row in a)
sold = (12.5 * int(n) for n in nppizza)
sum_sold = sum(sold)
print("sum:", sum_sold)