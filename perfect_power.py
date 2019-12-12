"""A perfect power is a classification of positive integers:
In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer. 
More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.
Your task is to check wheter a given integer is a perfect power. If it is a perfect power, return a pair m and k with mk = n as a proof. 
Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent.
Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions. 
However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.

Examples
isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None
"""




# too slow...
"""def isPP(n):
    for i in range(2,n//2):
      for j in range(2,n//2):
        if i**j == n:
          return [i, j]
    return None"""



# better, but still too slow...
"""def isPP(n):
    for j in range(2, n//2 + 1):
        if n**(1/j) in range(2, n//2 + 1):
            return [int(n**(1/j)), j]
    return None"""

# some clever guy's solution
"""
from math import ceil, log, sqrt

def isPP(n):
    for b in xrange(2, int(sqrt(n)) + 1):
        e = int(round(log(n, b)))
        if b ** e == n:
            return [b, e]
    return None
"""


# my solution, fast enough! ;)
def isPP(n):
    for i in range(2, n//2 + 1):
        tmp = n
        count = 0
        while tmp != 1:
            tmp /= i
            count += 1
            if tmp % i != 0:
                break
        if tmp == 1:
            return [i, count]
    return None
        

# let's try it!
print(isPP(4))
print(isPP(16))

pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]
for item in pp:
  print(isPP(item))