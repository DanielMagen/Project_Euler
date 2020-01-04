from decimal import *
def calc_sqrt_up_to_precision(num, precision):
    getcontext().prec = 4*precision
    low_estimate = Decimal(1)
    high_estimate = Decimal(num)
    num = Decimal(num)

    two = Decimal(2)

    for i in range(4*precision):
        average = (low_estimate + high_estimate) / two
        res = average**2
        if res == num:
            return average
        if res > num:
            high_estimate = average
            continue
        low_estimate = average

    return average

def sum_first_100_digits(num):
    up_to = 100
    num = str(num)
    summ = 0

    passed = 0
    for i in range(len(num)):
        try:
            summ += int(num[i])
            passed += 1
            if passed == up_to:
                return summ
        except:
            pass

    return summ


summ = 0
up_to = 100
for num in range(1, up_to + 1):
    if num**0.5 % 1 != 0:
        summ += sum_first_100_digits(calc_sqrt_up_to_precision(num, 100))

print(summ)