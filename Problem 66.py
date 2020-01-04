from math import floor, sqrt
from fractions import Fraction as frac

# taken from https://proofwiki.org/wiki/Continued_Fraction_Expansion_of_Irrational_Square_Root/Example/13
def get_continued_fraction_coefficients(D):
    sqrt_floored = floor(sqrt(D))

    P = [0]
    Q = [1]

    a = [floor(frac(sqrt_floored + P[-1], Q[-1]))]

    P.append(a[-1] * Q[-1] - P[-1])
    Q.append(frac(D - (P[-1] ** 2), Q[-1]))

    a.append(floor(frac(sqrt_floored + P[-1], Q[-1])))

    while True:
        P.append(a[-1] * Q[-1] - P[-1])
        Q.append(frac(D-(P[-1]**2), Q[-1]))

        if P[-1] == P[1] and Q[-1] == Q[1]:
            return a

        a.append(floor(frac(sqrt_floored + P[-1], Q[-1])))


# taken from https://proofwiki.org/wiki/Continued_Fraction_Expansion_of_Irrational_Square_Root/Example/13/Convergents
def get_continued_fraction(D):
    coefficients = get_continued_fraction_coefficients(D)
    p = [coefficients[0]]
    q = [1]

    yield p[-1], q[-1]

    p.append(coefficients[0] * coefficients[1] + 1)
    q.append(coefficients[1])

    yield p[-1], q[-1]

    k = 1
    coefficients = coefficients[1:]
    while True:
        p.append(coefficients[k%len(coefficients)] * p[k] + p[k-1])
        q.append(coefficients[k%len(coefficients)] * q[k] + q[k-1])

        k += 1

        yield p[-1], q[-1]


def check_if_is_solution(D,x,y):
    return x**2 - D*y**2 == 1


max_x = 0
D_for_max_x = 1
for D in range(2, 1001):
    if sqrt(D) % 1 != 0:
        gen = get_continued_fraction(D)
        while True:
            x, y = next(gen)
            is_solution = check_if_is_solution(D,x,y)
            if is_solution:
                if x > max_x:
                    max_x = x
                    D_for_max_x = D
                break


print(max_x)
print(D_for_max_x)
