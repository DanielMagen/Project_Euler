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


def generate_list_up_to(initial_list, to_power, up_to):
    lis = []
    for p in initial_list:
        new_num = p ** to_power
        if new_num < up_to:
            lis.append(new_num)
        else:
            break
    return lis

def sum_3_lists(lis1, lis2, lis3, up_to):
    new_lis = set([])
    for num1 in lis1:
        for num2 in lis2:
            if num1 + num2 >= upto:
                break
            for num3 in lis3:
                summ = num1 + num2 + num3
                if summ < upto:
                    new_lis.add(summ)
                else:
                    break
    return new_lis


upto = 50 * (10**6)
primes = prime_list(upto)
primes_squares = generate_list_up_to(primes, 2, upto)
primes_cubes = generate_list_up_to(primes, 3, upto)
primes_fourth = generate_list_up_to(primes, 4, upto)

new_lis = sum_3_lists(primes_squares, primes_cubes, primes_fourth, upto)
print(28 in new_lis)
print(47 in new_lis)
print(len(new_lis))