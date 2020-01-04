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

def get_all_prime_divisors(num, primes):
    divisors_list = []

    current_prime_index = 0
    while num!= 1 and current_prime_index < len(primes):
        if num%primes[current_prime_index]==0:
            num = num / primes[current_prime_index]
            divisors_list.append(primes[current_prime_index])
        else:
            current_prime_index+=1

    return divisors_list

def get_number_of_divisors(num, primes):
    prime_divisors = get_all_prime_divisors(num, primes)
    number_of_divisors = 1

    i = 0
    while i < len(prime_divisors):
        current_divisor = prime_divisors[i]
        times_current_divisor_showed = 1
        while i < len(prime_divisors) and prime_divisors[i] == current_divisor:
            times_current_divisor_showed += 1
            i += 1
        number_of_divisors *= times_current_divisor_showed

    return number_of_divisors


##### change of strategy
def for_each_natural_which_primes_divide_it(up_to, primes):
    natural_list = [[] for i in range(up_to + 1)]

    for prime in primes:
        for i in range(prime, len(natural_list), prime):
            natural_list[i].append(prime)

    return natural_list

def for_each_natural_how_many_divisors_it_has(up_to, primes):
    def get_number_of_divisors(prime_divisors):
        number_of_divisors = 1

        i = 0
        while i < len(prime_divisors):
            current_divisor = prime_divisors[i]
            times_current_divisor_showed = 1
            while i < len(prime_divisors) and prime_divisors[i] == current_divisor:
                times_current_divisor_showed += 1
                i += 1
            number_of_divisors *= times_current_divisor_showed

        return number_of_divisors

    def multiply_prime_divisors(num, prime_divisors):
        """
        gets a list of all prime divisors without knowing how
        many times each divisor divides the current number
        returns a list of prime divisors like get_all_prime_divisors
        """
        prime_divisors_multiplied = []
        for prime in prime_divisors:
            while num % prime == 0:
                prime_divisors_multiplied.append(prime)
                num = num // prime

        return prime_divisors_multiplied

    natural_list = for_each_natural_which_primes_divide_it(up_to, primes)

    natural_list[0] = 0
    natural_list[1] = 1

    for i in range(2, len(natural_list)):
        natural_list[i] = get_number_of_divisors(multiply_prime_divisors(i, natural_list[i]))

    return natural_list


up_to = 10**7
divisors_for_each_num = for_each_natural_how_many_divisors_it_has(up_to, prime_list(up_to))
number_has_same_number_of_divisors = 0

for i in range(2, len(divisors_for_each_num) - 1):
    if divisors_for_each_num[i] == divisors_for_each_num[i+1]:
        number_has_same_number_of_divisors += 1

print(number_has_same_number_of_divisors)