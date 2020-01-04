from math import factorial
remains = 10**6 - 1
next_fact = 9
digits = [i for i in range(10)]

while remains > 0:
    next_digit = remains // factorial(next_fact)
    print(digits[next_digit], end='')
    del(digits[next_digit])
    remains = remains - next_digit * factorial(next_fact)
    next_fact -= 1

for i in range(len(digits)):
    print(digits[i], end='')
