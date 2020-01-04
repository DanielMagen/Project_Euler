import math
upto = 1000
number_of_solutions_for_perimeter = [0 for i in range(upto + 1)]
for a in range(upto):
    a_squared = a**2
    for b in range(a, upto):
        if a + b > upto:
            break
        b_squared = b**2
        c = math.sqrt(a_squared+b_squared)
        if a + b + c > upto:
            break
        if c%1 != 0:
            continue
        c = int(c)
        number_of_solutions_for_perimeter[a+b+c]+=1

max_index = 0
max_solutions = number_of_solutions_for_perimeter[max_index]
for i in range(1, len(number_of_solutions_for_perimeter)):
    if number_of_solutions_for_perimeter[i] > max_solutions:
        max_solutions = number_of_solutions_for_perimeter[i]
        max_index = i

print(max_index)

