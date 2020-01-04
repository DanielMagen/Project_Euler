from math import factorial
up_to = factorial(9)
facts = [factorial(i) for i in range(10)]

def number_of_digits(num):
    return len(str(num))

def get_digit_number(num,digit_number):
    return int(str(num)[digit_number])

def sum_of_facts_of_digits(num):
    if number_of_digits(num) == 1:
        return facts[num]
    return facts[get_digit_number(num, -1)] + sum_of_facts_of_digits(num//10)

total_sum = 0
for i in range(3, up_to):
    if sum_of_facts_of_digits(i) == i:
        total_sum += i

print(total_sum)



