from fractions import Fraction as frac
import operator as op
from functools import reduce
from math import *

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    res = numer / denom
    if res % 1 == 0:
        return int(res)
    return res

count = 0
bigger_than = 10**6
for n in range(1,101):
    for r in range(1,n):
        if ncr(n, r) > bigger_than:
            count += 1
print(count)