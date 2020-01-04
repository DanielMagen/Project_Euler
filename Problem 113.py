def print_2d_table(table):
    for row in table:
        print(row)

up_to = 6

decreasing_table = [[0 for j in range(up_to)] for digit in range(10)]

for digit in range(10):
    decreasing_table[digit][0] = 1

for j in range(1, up_to):
    for digit in range(1, 10):
        res = 0

        if digit == 1 and j > 1:
            res +=1

        for previous_digit in range(digit + 1):
            res += decreasing_table[previous_digit][j-1]

            decreasing_table[digit][j] = res

summ = 0
for digit in range(len(decreasing_table)):
    summ += sum(decreasing_table[digit])


print_2d_table(decreasing_table)
print()

increasing_table = [[0 for j in range(up_to)] for digit in range(10)]

for digit in range(10):
    increasing_table[digit][0] = 1

for j in range(1, up_to):
    for digit in range(1, 10):
        res = 0
        for previous_digit in range(digit, 10):
            res += increasing_table[previous_digit][j-1]

            increasing_table[digit][j] = res


for digit in range(len(increasing_table)):
    summ += sum(increasing_table[digit])


print_2d_table(increasing_table)
print()
print(summ)
