up_to = 10**12

overall = [1]
for a in range(2, int(up_to**0.5)):
    list_of_repunits = []
    a_to_the_n = a
    current_result = (a_to_the_n - 1) // (a - 1)

    while current_result < up_to:
        list_of_repunits.append(current_result)
        a_to_the_n *= a
        current_result = (a_to_the_n - 1) // (a - 1)

    list_of_repunits.remove(a+1)
    list_of_repunits.remove(1)
    overall += list_of_repunits

print(sum(set(overall)))
