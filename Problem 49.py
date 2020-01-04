from itertools import permutations, combinations
def prime_list(up_to):
    natrual_list = [1 for i in range(up_to)]
    for i in range(2, int(len(natrual_list)**0.5) + 1):
        if natrual_list[i] == 0:
            continue
        for j in range(i**2, len(natrual_list), i):
            natrual_list[j] = 0

    list_of_primes = []
    for i in range(2, len(natrual_list)):
        if(natrual_list[i] == 1):
            list_of_primes.append(i)

    return list_of_primes

def list_to_str(lis):
    s = ""
    for item in lis:
        s += item
    return s

first_prime_after_1000 = 1009
primes = prime_list(10000)
primes = primes[primes.index(first_prime_after_1000):]
primes_set = set(primes)

def contains_arithmetic_progression_of_3(lis):
    """
    :param lis: a list of numbers
    :return: true if there is an arithmetic progression of length 3
    """
    for comb in combinations(lis, 3):
        if comb[2] - comb[1] == comb[1] - comb[0] != 0:
            return comb
    return False

def has_3_per_in_primes(num):
    num = str(num)
    pers_in_primes = []
    for per in permutations(num):
        if int(list_to_str(per)) in primes_set:
            pers_in_primes.append(int(list_to_str(per)))
    if len(pers_in_primes) < 3:
        return False
    return contains_arithmetic_progression_of_3(pers_in_primes)


primes_that_have_pers = []
for prime in primes:
    combinations_of_prime = has_3_per_in_primes(prime)
    if combinations_of_prime:
        primes_that_have_pers.append(combinations_of_prime)

print(primes_that_have_pers)
