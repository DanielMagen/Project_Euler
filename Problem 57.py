from fractions import Fraction as frac

def length_of_num(num):
    return len(str(num))

cuurent_frac = frac(1,2) + 1

count = 0
for i in range(999):
    cuurent_frac = 1/(cuurent_frac+1) + 1
    if length_of_num(cuurent_frac.denominator) < length_of_num(cuurent_frac.numerator):
        count += 1

print(count)


