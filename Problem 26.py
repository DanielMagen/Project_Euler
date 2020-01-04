from math import log, ceil

def find_cycle(num):
    cycle = ceil(log(num, 10))
    current_divide = 10**cycle % num

    while current_divide != 1:
        if current_divide == 0:
            return 0
        add_to_cycle = ceil(log(num/current_divide, 10))
        cycle += add_to_cycle
        last_divide = current_divide
        current_divide = (current_divide * 10 ** add_to_cycle) % num

        if last_divide == current_divide:
            return cycle - 1

    return cycle


maxx_rat = 0
maxx_num = 0
for i in range(1,1000):
    print(i)
    curr = find_cycle(i)
    if curr > maxx_rat:
        maxx_rat = curr
        maxx_num = i

print(maxx_rat)
print(maxx_num)
