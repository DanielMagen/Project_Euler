from math import ceil
def how_many_inside_of_size(small_rect_dim, large_rect_dim):
    summ = 1
    for i in range(len(small_rect_dim)):
        summ *= ceil(large_rect_dim[i] / small_rect_dim[i])
    return summ

def get_sum_of_ceilings(X):
    summ = 0
    for i in range(1, X + 1):
        summ += ceil(X / i)
    return summ

memory_map = {}
def get_sum_of_ceilings_mem(X):
    if X in memory_map:
        return memory_map[X]
    res = get_sum_of_ceilings(X)
    memory_map[X] = res
    return res

def how_many_inside(large_rect_dim):
    sum_R = 0
    sum_C = 0

    sum_R = get_sum_of_ceilings_mem(large_rect_dim[0])
    sum_C = get_sum_of_ceilings_mem(large_rect_dim[1])

    return sum_R * sum_C

def get_harmonic_numbers(upto):
    harmonic_numbers = [0 for i in range(upto +1)]
    for i in range(1, len(harmonic_numbers)):
        harmonic_numbers[i] = 1/i + harmonic_numbers[i-1]
    return harmonic_numbers

upto = 100
harmonic_numbers = get_harmonic_numbers(upto)
for i in range(2, upto):
    print(i, get_sum_of_ceilings_mem(i), ceil(i * harmonic_numbers[i]))
