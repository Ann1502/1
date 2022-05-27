A = [3, 4, 56, 100, 15, 2, 20, 30]
B = [i for i in A if i % 3 == 0 and i % 5 ==0]
import math
C = math.prod(B)
print (C)
