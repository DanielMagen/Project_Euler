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

def rotate(string_to_rotate):
    return string_to_rotate[len(string_to_rotate) - 1] + string_to_rotate[0:len(string_to_rotate) - 1]

def get_all_rotations_of_number(num):
    list_of_rotations = [str(num)]
    for i in range(len(str(num)) - 1):
        list_of_rotations.append(rotate(list_of_rotations[-1]))

    for i in range(len(list_of_rotations)):
        list_of_rotations[i] = int(list_of_rotations[i])

    return list_of_rotations


primes = prime_list(10**6)
primes_set = set(primes)

count = 0
for prime in primes:
    add = True
    for rot in get_all_rotations_of_number(prime):
        if rot not in primes_set:
            add = False
            break
    if add:
        count += 1

print(count)
