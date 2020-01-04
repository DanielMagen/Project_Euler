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

primes = prime_list(10**8)
biggest_prime = primes[-1]
primes = set(primes)

numbers_passed = 1
primes_passed = 0
current_number = 1
ratio = 1
jump_by = 0


while ratio > 0.1 and current_number <= biggest_prime:
    print(ratio, jump_by + 1)
    jump_by += 2
    for i in range(4):
        numbers_passed += 1
        current_number += jump_by
        if current_number in primes:
            primes_passed += 1

    ratio = primes_passed / numbers_passed

print(jump_by + 1)
