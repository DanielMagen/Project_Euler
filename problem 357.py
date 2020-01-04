from sympy import divisors

print("started")

up_to = ((10**6) * 100) + 1

natural_list = [1 for i in range(up_to)]
natural_list[1] = 0

prime_mark = 1
for i in range(2, int(len(natural_list) ** 0.5) + 1):
    if natural_list[i] == 0:
        continue
    for j in range(i ** 2, len(natural_list), i):
        natural_list[j] = 0

print("got to stage 2")

failure = 3
for i in range(2, len(natural_list)):
    if natural_list[i] == prime_mark:
        # check for all of hid multipliers if they are
        # 0) not marked with 3
        # a) 1 less than a prime
        # b) if mul/curr_prime + curr_prime is a prime
        # if they dont hold that condition mark them with 3
        for j in range(i ** 2, len(natural_list) - 1, i):
            if natural_list[j] == failure:
                continue
            if natural_list[j+1] != prime_mark:
                natural_list[j] = failure
                continue
            if natural_list[j//i + i] != prime_mark:
                natural_list[j] = failure
                continue


print("got to stage 3")

# now get all possible numbers
possible_numbers = [2]
primes = set([])
for i in range(1, len(natural_list)):
    if natural_list[i] != failure and natural_list[i] != prime_mark:
        possible_numbers.append(i)
    else:
        if natural_list[i] == prime_mark:
            primes.add(i)


# now we have possible candidates
# check them using brute force
print(len(possible_numbers))
print(len(primes))

#print(possible_numbers)

print("got to stage 4")

passed = []
for i in range(len(possible_numbers)):
    if i % 10000 == 0:
        print("currently in", i)

    to_add = True
    divos = divisors(possible_numbers[i])
    for j in range(len(divos)//2 + 1):
        if divos[j] + divos[-j-1] not in primes:
            to_add = False
            break
    if to_add:
        passed.append(possible_numbers[i])

print(sum(passed))


