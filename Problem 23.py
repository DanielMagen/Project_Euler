from sympy import divisors
import itertools as it

abundants = [i for i in range(1,28124) if i+i < sum(divisors(i))]
sum_of_abundants = {i+j for i, j in it.product(abundants, repeat=2)}

sum_of_numbers_cant_be_written_as_sum_of_abundants = 0
for i in range(28124):
    if i not in sum_of_abundants:
        sum_of_numbers_cant_be_written_as_sum_of_abundants += i

print(sum_of_numbers_cant_be_written_as_sum_of_abundants)

