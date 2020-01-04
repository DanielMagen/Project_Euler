from itertools import combinations

def list_to_str(lis):
    s = ""
    for item in lis:
        s += str(item)
    return s

def split_num(num):
    num = str(num)
    lis = []
    for c in num:
        lis.append(int(c))
    return lis

def numbers_are_permutation(num1, num2):
    lis1 = sorted(split_num(num1))
    lis2 = sorted(split_num(num2))
    str1 = list_to_str(lis1)
    str2 = list_to_str(lis2)
    return str1 == str2

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
    natrual_list[1] = 1
    return natrual_list


phi = phi_list(10**7)
min_rat = 10000
min_i = 1
for i in range(2, len(phi)):
    if numbers_are_permutation(i, phi[i]):
        rat = i / phi[i]
        if rat < min_rat:
            min_rat = rat
            min_i = i

print(min_i)
print(min_rat)

