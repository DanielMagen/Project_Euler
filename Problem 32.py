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

products_that_appeared = set([])
total_sum = 0
for a in range(1,100):

    str_a = str(a)

    if has_0(str_a) or has_repeating_digits(str_a):
        continue

    for b in range(a+1, 2000):
        str_b = str(b)

        if has_0(str_b) or has_repeating_digits(str_b):
            continue
        if share_digit(str_a, str_b):
            continue

        product = a*b
        str_product = str(product)

        if has_0(str_product) or has_repeating_digits(str_product):
            continue

        if share_digit(str_a, str_product):
            continue
        if share_digit(str_b, str_product):
            continue

        digits_a = get_digits(str_a)
        digits_b = get_digits(str_b)
        digits_product = get_digits(str_product)

        if contains_1_to_9(digits_a | digits_b | digits_product):
            if product not in products_that_appeared:
                products_that_appeared.add(product)
                total_sum += product

print(total_sum)

