def count_digits(num):
    return len(str(num))

upto = 1000
list_of_powers = [i for i in range(upto + 1)]

count = 0
for power in range(1, 500):
    for i in range(1, len(list_of_powers)):
        if count_digits(list_of_powers[i]) == power:
            count += 1
        list_of_powers[i] *= i
    print(count)

