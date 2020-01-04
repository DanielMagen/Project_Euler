from math import sqrt
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

def squares_list(up_to):
    return [i**2 for i in range(up_to + 1)]

up_to = 10000
primes = prime_list(up_to)
squares = squares_list(int(sqrt(up_to)))

nats = [i for i in range(up_to * 2)]
nats[0] = 1
for prime in primes:
    nats[prime] = 0
    for square in squares:
        summ = prime + 2*square
        if summ < len(nats):
            nats[summ] = 0

for i in range(len(nats)):
    if nats[i] != 0 and nats[i]%2 != 0:
        print(i)