def get_rad_list(up_to):
    composite_mark = 1
    natural_list = [i for i in range(up_to)]
    for i in range(2, int(len(natural_list)**0.5) + 1):
        if natural_list[i] == composite_mark:
            continue
        for j in range(i**2, len(natural_list), i):
            natural_list[j] = composite_mark

    list_of_rad = natural_list.copy()

    for i in range(2, len(list_of_rad)):
        if natural_list[i] != composite_mark:
            for j in range(i*2, len(natural_list), i):
                list_of_rad[j] *= natural_list[i]

    # now turn every item in the list_of_rad into a tuple of the
    # original number and its rad
    for i in range(len(list_of_rad)):
        list_of_rad[i] = (list_of_rad[i], i)

    return list_of_rad


rad_list = get_rad_list(10**5 + 1)
rad_list.sort()
print(rad_list[10**4][1])

