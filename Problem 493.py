import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    res = numer / denom
    if res % 1 == 0:
        return int(res)
    return res


print(7*(1 - ncr(60,20)/ncr(70,20)))
print('a.bcdefghij')