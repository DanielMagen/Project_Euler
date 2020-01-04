def get_digits(num):
    #num = str(num)
    digits_set = set([])
    for i in range(len(num)):
        digits_set.add(int(num[i]))
    return digits_set

def share_digit(num1, num2):
    #num1 = str(num1)
    #num2 = str(num2)
    for digit in num1:
        if digit in num2:
            return True
    return False

def has_repeating_digits(num):
    #num = str(num)
    digits_set = set([])
    for i in range(len(num)):
        if int(num[i]) in digits_set:
            return True
        digits_set.add(int(num[i]))
    return False

def contains_1_to_9(some_set):
    for i in range(1,10):
        if i not in some_set:
            return False
    return True

def has_0(num):
    return '0' in num  # str(num)

def concatenate_ints(int1, int2):
    return int(str(int1) + str(int2))

max_canc = 0
for i in range(2, 10000):
    str_i = str(i)

    if has_0(str_i) or has_repeating_digits(str_i):
        continue

    current_canc = i
    current_multiply = 2
    while True:
        current_canc = concatenate_ints(current_canc, i*current_multiply)
        current_canc_str = str(current_canc)
        if len(current_canc_str) > 9:
            break
        if has_0(current_canc_str) or has_repeating_digits(current_canc_str):
            break
        if contains_1_to_9(get_digits(current_canc_str)):
            if current_canc > max_canc:
                max_canc = current_canc
            break

print(max_canc)

