from itertools import product

def get_number_of_throws_that_lead_to_each_possible_result(cube_sides_list, number_of_throws):
    # assume cube_sides_list is sorted
    max_val =  cube_sides_list[-1] * number_of_throws
    number_of_throws_that_lead_to_each_possible_result = [0 for i in range(max_val+1)]
    for dice_throw in product(cube_sides_list, repeat=number_of_throws):
        number_of_throws_that_lead_to_each_possible_result[sum(dice_throw)] += 1
    return number_of_throws_that_lead_to_each_possible_result

def get_list_of_sum(lis):
    list_of_sum = [lis[0]]
    for i in range(1, len(lis)):
        list_of_sum.append(list_of_sum[-1] + lis[i])
    return list_of_sum


def divide_each_item_in_list(lis, divide_by):
    for i in range(len(lis)):
        lis[i] = lis[i] / divide_by

    return lis

def get_how_many_possible_throws(cube_sides_list, number_of_throws):
    return len(cube_sides_list)**number_of_throws

def get_probabilities(cube_sides_list, number_of_throws):
    divide_by = get_how_many_possible_throws(cube_sides_list, number_of_throws)
    number_of_throws_that_lead_to_each_possible_result = get_number_of_throws_that_lead_to_each_possible_result(cube_sides_list, number_of_throws)
    return divide_each_item_in_list(number_of_throws_that_lead_to_each_possible_result, divide_by)

def get_cumulative(cube_sides_list, number_of_throws):
    return get_list_of_sum(get_number_of_throws_that_lead_to_each_possible_result(cube_sides_list, number_of_throws))


def get_cumulative_distribution(cube_sides_list, number_of_throws):
    possibilities = get_cumulative(cube_sides_list, number_of_throws)
    how_many_throws = get_how_many_possible_throws(cube_sides_list, number_of_throws)

    return divide_each_item_in_list(possibilities, how_many_throws)

"""
cube_sides_list = [1,2,3]
number_of_throws = 2
print(get_number_of_throws_that_lead_to_each_possible_result(cube_sides_list, number_of_throws))
print(get_probabilities(cube_sides_list, number_of_throws))

"""
peter_dice = [i for i in range(1, 5)]
peter_throws = 9

colin_dice = [i for i in range(1, 7)]
colin_throws = 6

# now calculate the probability that Pete beats Colin
pete_probabilities = get_probabilities(peter_dice, peter_throws)
colin_probabilities = get_cumulative_distribution(colin_dice, colin_throws)

total = 0
for i in range(1, len(pete_probabilities)):
    total += pete_probabilities[i] * colin_probabilities[i-1]

print(total)
print('0.abcdefg')
# manually round to nearest digit
