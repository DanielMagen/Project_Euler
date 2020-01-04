from sympy import divisors

def get_right_truncatable_harshad_number_up_to_len(length):
    current_length = 1
    overall_harshad_numbers = []
    harshad_numbers_of_current_length = [i for i in range(1, 10)]
    sum_of_digits_of_current_harshad_numbers = [i for i in range(1, 10)]

    overall_harshad_numbers += harshad_numbers_of_current_length

    while current_length < length:
        new_harshad_numbers = []
        sum_of_digits_of_new_harshad_numbers = []

        for i in range(len(harshad_numbers_of_current_length)):
            num = harshad_numbers_of_current_length[i]
            num_digits_sum = sum_of_digits_of_current_harshad_numbers[i]
            num_times_10 = num * 10
            for digit in range(10):
                # check if adding the another digit conserves the harshadity of the number
                temp_num = num_times_10 + digit
                temp_num_digit_sum = num_digits_sum + digit
                if temp_num % temp_num_digit_sum == 0:
                    new_harshad_numbers.append(temp_num)
                    sum_of_digits_of_new_harshad_numbers.append(temp_num_digit_sum)

        current_length += 1
        harshad_numbers_of_current_length = new_harshad_numbers
        sum_of_digits_of_current_harshad_numbers = sum_of_digits_of_new_harshad_numbers

        overall_harshad_numbers += harshad_numbers_of_current_length

    return overall_harshad_numbers

def number_is_prime(num):
    return len(divisors(num)) == 2

def str_to_list(string):
    lis = []
    for c in string:
        lis.append(c)
    return lis

def get_sum_of_digits(num):
    digits = str(num)
    digits = str_to_list(digits)

    summ = 0
    for i in range(len(digits)):
        summ += int(digits[i])
    return summ

length = 14
harshad_numbers = get_right_truncatable_harshad_number_up_to_len(length)

# now filter them to only strong harshad numbers
strong_harshad_numbers = []
for num in harshad_numbers:
    num_digits_sum = get_sum_of_digits(num)
    prime_candidate = num // num_digits_sum
    if number_is_prime(prime_candidate):
        strong_harshad_numbers.append(num)

# now use this list to find all strong right truncatable Harshad primes less than 10**14
strong__right_truncatable_harshad_numbers = []

up_to = 10**length
for num in strong_harshad_numbers:
    num_times_10 = num * 10
    for digit in [1,3,5,7,9]:
        # check if adding the another digit makes it a prime
        prime_candidate = num_times_10 + digit
        if prime_candidate < up_to:
            if number_is_prime(prime_candidate):
                strong__right_truncatable_harshad_numbers.append(prime_candidate)

#print(strong__right_truncatable_harshad_numbers)
print(sum(strong__right_truncatable_harshad_numbers))
