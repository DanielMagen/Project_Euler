from fractions import Fraction as frac

def get_e_sequence(size):
    lis = []
    i = 1
    while len(lis) < size:
        lis += [1, 2*i, 1]
        i += 1
    return lis[:size]

def get_e_term(e_sequence):
    if len(e_sequence) == 1:
        return e_sequence[0]
    return e_sequence[0] + frac(1, get_e_term(e_sequence[1:]))

def str_to_list(string):
    lis = []
    for c in string:
        lis.append(c)
    return lis

def get_sum_of_digits(num):
    digits = str(num)
    digits = str_to_list(digits)

    summ = 0
    for i in range(len(digits)):
        summ += int(digits[i])
    return summ

up_to = 100
e_sequence = get_e_sequence(up_to - 1)
e = 2 + frac(1, get_e_term(e_sequence))
print(get_sum_of_digits(e.numerator))