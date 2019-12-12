

# not fast enough...
"""def primeFactors(n):
    tmp = n
    sols = ''
    for i in range(2, n//2 + 1):
        count = 0
        while tmp % i == 0:
            tmp //= i
            count += 1
            if tmp % i != 0:
                if count == 1:
                    sols += f'({i})'
                else:
                    sols += f'({i}**{count})'
                break
    return sols"""

# still not fast enough...
def primeFactors(n):
    tmp = n
    sols = []
    for i in range(2, int(n**0.5 + 1)):
        if tmp % i == 0:
            count = 0
            while True:
                tmp //= i
                count += 1
                if tmp % i != 0:
                    if count == 1:
                        sols.append(f'({i})')
                    else:
                        sols.append(f'({i}**{count})')
                    break
    return ''.join(sols)

# let's try it!
print(primeFactors(86240))
print(primeFactors(86240) == "(2**5)(5)(7**2)(11)")

# let's test it!
assert primeFactors(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)"
print('Test is OK!')
