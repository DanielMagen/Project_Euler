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

primes_set = set(prime_list(10000000))

def find_how_many_primes(func):
    count = 0
    current_n = 0
    while True:
        if func(current_n) in primes_set:
            count+=1
            current_n += 1
        else:
            break
    return count

maximum_count = 0
maximum_a = 0
maximum_b = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        func = lambda i: i**2 + a*i + b
        result = find_how_many_primes(func)
        if result > maximum_count:
            maximum_count = result
            maximum_a = a
            maximum_b = b
            
print(maximum_a*maximum_b)