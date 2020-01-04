from math import sqrt

def get_main_term(i):
    return i*(3*i-1)

min_diff = 100000000000
for a in range(1,10000):
    a_main_term = get_main_term(a)
    if a % 1000 == 0:
        print('current min', min_diff)

    for b in range(a+1, 10000):
        b_main_term = get_main_term(b)

        # check if their sum is pentagonal
        terms_sum = a_main_term + b_main_term
        discriminant = sqrt(1 + 12*terms_sum)
        if discriminant % 1 != 0:
            continue
        c = int(discriminant) + 1
        if c%6 != 0:
            continue

        # check if their difference is pentagonal
        terms_diff = b_main_term - a_main_term
        discriminant = sqrt(1 + 12 * terms_diff)
        if discriminant % 1 != 0:
            continue
        c = int(discriminant) + 1
        if c % 6 != 0:
            continue

        diff = terms_diff/2
        if diff < min_diff:
            min_diff = diff

print(min_diff)


