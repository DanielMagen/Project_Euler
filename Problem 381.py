from math import factorial

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

# from wiki books
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def calc_S(prime):
    # now my method
    fact = prime - 1
    summ = fact
    for i in range(prime - 1, prime - 5, -1):
        fact *= modinv(i, prime)
        fact = fact % prime
        summ += fact

    return summ % prime

up_to = 10**8
primes = prime_list(up_to)
print("finished calculating primes")
summ = 0
for i in range(2, len(primes)):
    summ += calc_S(primes[i])

print(summ)


