import math

multiples = [0 for x in range(1000000)]

# creates a list such that each number has the number of unique primes that divides it
# in its corresponding index
for i in range(2, int(math.sqrt(len(multiples))) + 1):
    if multiples[i] == 0:
        for j in range(i * 2, len(multiples), i):
            multiples[j] += 1

for i in range(len(multiples)-4):
    if multiples[i] == multiples[i+1] == multiples[i+2] == multiples[i+3] == 4:
        print(i)
        break
