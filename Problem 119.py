max_power = 10

def get_digits_sum(num):
    num = str(num)
    summ = 0
    for i in range(len(num)):
        summ += int(num[i])
    return summ

hold = []
for num in range(2, 100):
    current_num = num
    if num > 9:
        current_num_sum_of_digits = get_digits_sum(current_num)
        if current_num_sum_of_digits == num:
            #print(num, '^', 1, '=', current_num)
            hold.append(current_num)
    for power in range(1, max_power):
        current_num *= num
        current_num_sum_of_digits = get_digits_sum(current_num)
        if current_num_sum_of_digits == num:
            #print(num, '^', power + 1, '=', current_num)
            hold.append(current_num)

print(sorted(hold)[29])