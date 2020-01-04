def number_of_digits(num):
    return len(str(num))

def get_digit_number(num,digit_number):
    return int(str(num)[digit_number])

up_to = 1000001
digits_to_get = [1,10,100,1000,10000,100000,1000000]
total_digits_passed = 0
current_num = 0
next_digit_to_search = 0
total_multiple_of_digits = 1

while total_digits_passed < up_to:
    digits = number_of_digits(current_num)

    if total_digits_passed + digits > digits_to_get[next_digit_to_search]:
        # find the digit
        digit_to_get_in_current_num = total_digits_passed - digits_to_get[next_digit_to_search]
        print(current_num, digit_to_get_in_current_num)
        total_multiple_of_digits *= get_digit_number(current_num, digit_to_get_in_current_num)

        next_digit_to_search += 1

    current_num += 1
    total_digits_passed += digits

print(total_multiple_of_digits)