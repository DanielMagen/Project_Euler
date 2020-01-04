from fractions import Fraction as frac
from math import floor

upto = 10**6 + 1
max_frac = 0
for d in range(2, upto):
    if d % 7 == 0:
        continue
    new_frac = frac(floor(3*(d/7)), d)
    if new_frac > max_frac:
        max_frac = new_frac

print(max_frac)
