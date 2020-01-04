from sympy import divisors
up_to = 10001
sums_of_divisors = [0] + [sum(divisors(i))-i for i in range(1, up_to)]
total_sum = 0
for i in range(1, len(sums_of_divisors)):
    current_divisor_sum = sums_of_divisors[i]
    if current_divisor_sum != i:
        if current_divisor_sum < len(sums_of_divisors):
            if sums_of_divisors[current_divisor_sum] == i:
                total_sum += i

print(total_sum)