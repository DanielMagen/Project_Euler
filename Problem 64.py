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

up_to = 10000
count = 0
for N in range(2, up_to + 1):
    if sqrt(N) % 1 != 0:
        coefficients = get_continued_fraction_coefficients(N)
        if len(coefficients) % 2 == 0:
            count += 1

print(count)
