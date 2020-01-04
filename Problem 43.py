from itertools import permutations
def get_digits(num_str, digits):
    digits = str(digits)
    new_num = ""
    for d in digits:
        new_num += num_str[int(d)]
    return int(new_num)

primes = [2,3,5,7,11,13,17]

def check_condition(num_str):
    for i in range(1, 8):
        digits = str(i) + str(i+1) + str(i+2)
        new_num = get_digits(num_str, digits)
        if new_num % primes[i-1] != 0:
            return False
    return True

def list_to_str(lis):
    s = ""
    for item in lis:
        s += item
    return s

pers = "0123456789"
summ = 0
for per in permutations(pers):
    if check_condition(per):
        summ += int(list_to_str(per))

print(summ)

