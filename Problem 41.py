from itertools import permutations
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

primes = prime_list(10**5)

def is_prime(num):
    for prime in primes:
        if num % prime == 0:
            return False
    return True

def list_to_str(lis):
    s = ""
    for item in lis:
        s += item
    return s

pers = "1234567"
for per in permutations(pers):
    num = int(list_to_str(per))
    if is_prime(num):
        print(num)