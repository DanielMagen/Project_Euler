from math import log, ceil
def get_k_such_that_a_less_than_b_times_10_to_k(a, b):
    return ceil(log(a/b, 10))

def get_cycle(a):
    b = 1
    seen = [b]

    while True:
        b *= 10**get_k_such_that_a_less_than_b_times_10_to_k(a,b)
        b = b % a
        if b == 0:
            return 0
        if b in seen:
            return len(seen) - seen.index(b)
        seen.append(b)


max_cycle = 0
max_d = 0
for d in range(2,1000):
    cycle = get_cycle(d)
    if cycle > max_cycle:
        max_cycle = cycle
        max_d = d

print(max_d)