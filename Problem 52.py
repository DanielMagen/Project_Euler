def get_digits(num):
    num = str(num)
    digits_set = set([])
    for i in range(len(num)):
        digits_set.add(int(num[i]))
    return digits_set

current_num = 1
while True:
    digits = get_digits(current_num)
    to_print = True
    for i in range(2, 7):
        digits2 = get_digits(current_num*i)
        if digits != digits2:
            to_print = False
            break
    if to_print:
        print(current_num)
        break

    current_num += 1


