def number_of_digits(num):
    return len(str(num))

def get_digit_number(num,digit_number):
    return int(str(num)[digit_number])

def sum_of_squares_of_digits(num):
    if number_of_digits(num) == 1:
        return num**2
    return get_digit_number(num, -1)**2 + sum_of_squares_of_digits(num//10)



upto = 10000000
numbers = [i for i in range(upto + 1)]
continue_loop = True

print("gt")

while continue_loop:
    reps = set([])
    for i in range(1, len(numbers)):
        sum_of_squares_of_digits_of_rep = sum_of_squares_of_digits(numbers[i])
        numbers[i] = numbers[sum_of_squares_of_digits_of_rep]

    for i in range(1, len(numbers)):
        reps.add(numbers[i])

    if len(reps) <= 2:
        continue_loop = False

count = 0
for i in range(1, len(numbers)):
    if numbers[i] != 1:
        count += 1
print(count)



