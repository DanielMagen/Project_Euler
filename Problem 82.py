def increase_location_by(lis, location, increase_by):
    new_lis = lis.copy()
    new_lis[location] += increase_by
    return new_lis

def get_indices_that_can_be_solved(index_pair, matrix_bounds_pair, rule_function):
    possible_indices = []
    for i in range(len(index_pair)):
        new_pair = increase_location_by(index_pair, i, 1)
        if new_pair[i] >= 0 and new_pair[i] < matrix_bounds_pair[i]:
            possible_indices.append(new_pair)

        new_pair = increase_location_by(index_pair, i, -1)
        if new_pair[i] >= 0 and new_pair[i] < matrix_bounds_pair[i]:
            possible_indices.append(new_pair)

    i = 0
    while i < len(possible_indices):
        is_valid = rule_function(index_pair, possible_indices[i])
        if is_valid:
            i += 1
        else:
            del possible_indices[i]

    return possible_indices


# 0th index = row, 1th index = col
# rows increase down, cols increase right
def up_rule(index_pair, index_pair_that_should_be_down):
    if index_pair[1] == index_pair_that_should_be_down[1]:
        return index_pair[0] - index_pair_that_should_be_down[0] == -1
    return False

def down_rule(index_pair, index_pair_that_should_be_up):
    if index_pair[1] == index_pair_that_should_be_up[1]:
        return index_pair[0] - index_pair_that_should_be_up[0] == 1
    return False

def left_rule(index_pair, index_pair_that_should_be_right):
    if index_pair[0] == index_pair_that_should_be_right[0]:
        return index_pair[1] - index_pair_that_should_be_right[1] == -1
    return False

def right_rule(index_pair, index_pair_that_should_be_left):
    if index_pair[0] == index_pair_that_should_be_left[0]:
        return index_pair[1] - index_pair_that_should_be_left[1] == 1
    return False

def up_down_right_rule(index_pair,index_pair_that_should_be_up_down_left):
    if up_rule(index_pair, index_pair_that_should_be_up_down_left):
        return True

    if down_rule(index_pair, index_pair_that_should_be_up_down_left):
        return True

    if right_rule(index_pair, index_pair_that_should_be_up_down_left):
        return True

    return False

def get_matrix_value(matrix, indices):
    curr = matrix
    for i in range(len(indices)-1):
        curr = curr[indices[i]]
    return curr[indices[-1]]

def set_matrix_value(matrix, indices, value):
    curr = matrix
    for i in range(len(indices)-1):
        curr = curr[indices[i]]
    curr[indices[-1]] = value


def find_minimum_path_from(matrix, row_in_first_col, row_in_last_col):
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0])
    matrix_bounds_pair = [matrix_rows, matrix_cols]

    rule_function = up_down_right_rule

    minimum_path = [[None for j in range(matrix_cols)] for i in range(matrix_rows)]

    known = [row_in_last_col, matrix_cols-1]
    set_matrix_value(minimum_path, known, get_matrix_value(matrix, known))

    prev_gen = []
    current_gen = [known]
    to_add_to_current_gen = []
    # we will get to some indices before we can solve them
    # so we keep those indices and keep checking if we can solve them later

    while len(current_gen) > 0:
        prev_gen = current_gen
        current_gen = set([])

        # need to do all at once



        # set possible next gen
        for index_pair in prev_gen:
            current_gen.add(get_indices_that_can_be_solved(index_pair, matrix_bounds_pair, rule_function))

        # remove all those that were already solved
        current_gen = list(current_gen)
        i = 0
        while i < len(current_gen):
            if get_matrix_value(minimum_path, current_gen[i]) is not None:
                del current_gen[i]
            else:
                i += 1

        current_gen += to_add_to_current_gen
        # now set aside all those who

        # now current gen holds all those that need and can be solved
        for index_pair in current_gen:



