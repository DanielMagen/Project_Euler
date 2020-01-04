def prime_list(up_to):
    prime_mark = 1
    natural_list = [prime_mark for i in range(up_to)]
    for i in range(2, int(len(natural_list)**0.5) + 1):
        if natural_list[i] == 0:
            continue
        for j in range(i**2, len(natural_list), i):
            natural_list[j] = 0

    list_of_primes = []
    for i in range(2, len(natural_list)):
        if natural_list[i] == prime_mark:
            list_of_primes.append(i)

    return list_of_primes

def get_list_for_numbers_up_to_inclusive(lis, upper):
    i = len(lis) - 1
    new_lis = []
    while i > -1:
        if lis[i] <= upper:
            return lis[:i+1]

        i -= 1

    return []

up_to = 10**8
primes = prime_list(up_to//2)
total = 0
while len(primes) > 1:
    total += len(primes)
    primes = get_list_for_numbers_up_to_inclusive(primes[1:], up_to / primes[1])

print(total)