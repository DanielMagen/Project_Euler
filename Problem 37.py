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

def get_list_of_truncs(num):
    num = str(num)
    lis = []
    for i in range(len(num) - 1):
        lis.append(int(num[:i+1]))
    for i in range(1, len(num)):
        lis.append(int(num[i:]))
    return lis

primes = prime_list(1000000)
primes_set = set(primes)

list_of_trunc_primes = []
for i in range(5, len(primes)):
    to_add = True
    for num in get_list_of_truncs(primes[i]):
        if num not in primes_set:
            to_add = False
            break
    if to_add:
        list_of_trunc_primes.append(primes[i])

print(sum(list_of_trunc_primes))
