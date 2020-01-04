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


upto = 10**6
primes = prime_list(2 * upto)
primes_set = set(primes)

primes_to_try = primes.copy()
try_for = 1000
print_below = 10

for j in range(1, try_for):
    for i in range(len(primes)//2):
        primes_to_try[i] += primes[i+j]

    # now check which ones a prime
    still_prime = []
    for i in range(len(primes) // 2):
        if primes_to_try[i] in primes_set:
            still_prime.append(primes_to_try[i])


    if j > 20 and len(still_prime) != 0:
        maxx = 0
        for p in still_prime:
            if p >= upto:
                break
            if p > maxx:
                maxx = p
        print(maxx)


