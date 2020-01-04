from itertools import combinations

def multiply_list(lis):
    mul = 1
    for item in lis:
        mul *= item

    return mul

def phi_list(up_to):
    natrual_list = [[] for i in range(up_to + 1)]
    for i in range(2, len(natrual_list)):
        if len(natrual_list[i]) != 0:
            continue
        for j in range(i, len(natrual_list), i):
            natrual_list[j].append(i)

    for i in range(2, len(natrual_list)):
        phi = i
        for sub in range(1, len(natrual_list[i]) + 1):
            current_sign = (-1)**sub
            denominators = list(combinations(natrual_list[i], sub))
            summ = 0
            for d in denominators:
                summ += i//multiply_list(d)
            phi += current_sign * summ

        natrual_list[i] = phi

    natrual_list[0] = 0
    natrual_list[1] = 0
    return natrual_list


phi = phi_list(10**6)
max_rat = 1
max_i = 1
for i in range(2, len(phi)):
    rat = i / phi[i]
    if rat > max_rat:
        max_rat = rat
        max_i = i

print(max_i)
print(max_rat)
