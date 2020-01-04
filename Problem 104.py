def get_digits(num):
    num = str(num)
    digits_set = set([])
    for i in range(len(num)):
        digits_set.add(int(num[i]))
    return digits_set

def contains_exactly_1_to_9(some_set):
    if len(some_set) == 9:
        if 0 not in some_set:
            return True
    return False

def get_first_digits(num, how_many_digits):
    num = str(num)
    return int(num[:how_many_digits])

def fibonacci(up_to):
    digits = 9
    max_digits = 10**digits
    f = [1, 1]
    for i in range(3, up_to + 1):
        new_number = (f[-2] + f[-1])
        f[-2] = f[-1]
        f[-1] = new_number
        digits_of_current_number_of_last_9 = get_digits(f[-1] % max_digits)
        if contains_exactly_1_to_9(digits_of_current_number_of_last_9):
            if contains_exactly_1_to_9(get_digits(get_first_digits(f[-1], 9))):
                print(i)
    return f

up_to = 1000000
fibonacci(up_to)
