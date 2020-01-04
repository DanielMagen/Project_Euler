from fractions import Fraction as frac

def share_digit(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    for digit in num1:
        if digit in num2:
            return int(digit)
    return -1

def remove_digit(num, digit):
    num = str(num)
    index = num.index(str(digit))
    newnum = num[:index] + num[index+1:]
    return int(newnum)


final_frac = frac(1,1)
for i in range(10,100):
    for j in range(i+1, 100):
        shared_digit = share_digit(i,j)
        if shared_digit == -1 or shared_digit == 0:
            continue
        frac1 = frac(i,j)
        newi = remove_digit(i,shared_digit)
        newj = remove_digit(j,shared_digit)
        if newj == 0:
            continue
        frac2 = frac(newi, newj)
        if frac1 - frac2 == 0:
            final_frac *= frac(i,j)

print(final_frac)