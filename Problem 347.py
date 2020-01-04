def prime_list(up_to):
    prime_mark = 1
    natural_list = [prime_mark for i in range(up_to + 1)]
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

def for_each_natural_which_primes_divide_it(up_to, primes):
    natural_list = [[] for i in range(up_to + 1)]

    for prime in primes:
        for i in range(prime, len(natural_list), prime):
            natural_list[i].append(prime)

    return natural_list


up_to = 10**7
divisors_for_each_num = for_each_natural_which_primes_divide_it(up_to, prime_list(up_to))

# remove all those with more or less than 2 divisors
for i in range(len(divisors_for_each_num)):
    if len(divisors_for_each_num[i]) != 2:
        divisors_for_each_num[i] = []
    else:
        # change them to tuple so that they could be indexed in a set
        divisors_for_each_num[i] = tuple(divisors_for_each_num[i])

# now calculate the sum
summ = 0
pairs_met = set([])
for i in range(len(divisors_for_each_num)-1, -1, -1):
    if len(divisors_for_each_num[i]) != 0:
        if divisors_for_each_num[i] not in pairs_met:
            # we got a hit
            summ += i
            pairs_met.add(divisors_for_each_num[i])

print(summ)
