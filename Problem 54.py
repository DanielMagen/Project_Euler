######### has some sort of a bug
# fuck it

card_value_numeric = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

player_1_wins = 1
player_2_wins = -1
draw = 0

def split_card_into_value_and_type(card):
    return [card_value_numeric[card[0]], card[1]]

def is_consecutive(lis):
    for i in range(1,len(lis)):
        if abs(lis[i] - lis[i-1]) != 1:
            if lis[-1] != card_value_numeric['A']:
                return False
            if lis[0] != card_value_numeric['2']:
                return False
    return True

def parse_hand_into_2_players(hand):
    hand = hand.split(' ')

    player_1_values = []
    player_1_types = []
    for i in range(5):
        value, type_of_card = split_card_into_value_and_type(hand[i])
        player_1_values.append(value)
        player_1_types.append(type_of_card)

    player_2_values = []
    player_2_types = []
    for i in range(5, 10):
        value, type_of_card = split_card_into_value_and_type(hand[i])
        player_2_values.append(value)
        player_2_types.append(type_of_card)

    player_1 = [player_1_values, player_1_types]
    player_2 = [player_2_values, player_2_types]

    return player_1, player_2


def compare_highest_value_cards(player_1, player_2):
    def get_highest_value_card(player):
        player_values = player[0]
        return max(player_values)

    player_1_highest = get_highest_value_card(player_1)
    player_2_highest = get_highest_value_card(player_2)

    if player_1_highest > player_2_highest:
        return player_1_wins

    if player_2_highest > player_1_highest:
        return player_2_wins

    return draw


def compare_2_pairs(player_1, player_2):
    def get_all_values_pairs(player):
        player_values = sorted(player[0])
        pairs = set([])
        for i in range(len(player_values)-1):
            if player_values[i] == player_values[i+1]:
                pairs.add(player_values[i])

        return sorted(pairs, reverse=True)  # biggest value at the beginning

    player_1_pairs = get_all_values_pairs(player_1)
    player_2_pairs = get_all_values_pairs(player_2)

    if len(player_1_pairs) > len(player_2_pairs):
        return player_1_wins

    if len(player_2_pairs) > len(player_1_pairs):
        return player_2_wins

    for i in range(len(player_1_pairs)):
        if player_1_pairs[i] > player_2_pairs[i]:
            return player_1_wins

        if player_2_pairs[i] > player_1_pairs[i]:
            return player_2_wins

    return draw


def three_of_a_kind(player_1, player_2):
    def get_all_values_triples(player):
        player_values = sorted(player[0])
        triples = set([])
        for i in range(len(player_values)-2):
            if player_values[i] == player_values[i+1] == player_values[i+2]:
                triples.add(player_values[i])

        return sorted(triples, reverse=True)  # biggest value at the beginning

    player_1_pairs = get_all_values_triples(player_1)
    player_2_pairs = get_all_values_triples(player_2)

    if len(player_1_pairs) > len(player_2_pairs):
        return player_1_wins

    if len(player_2_pairs) > len(player_1_pairs):
        return player_2_wins

    for i in range(len(player_1_pairs)):
        if player_1_pairs[i] > player_2_pairs[i]:
            return player_1_wins

        if player_2_pairs[i] > player_1_pairs[i]:
            return player_2_wins

    return draw


def straight(player_1, player_2):
    player_1_values = sorted(player_1[0])
    player_2_values = sorted(player_2[0])

    player_1_is_consecutive = is_consecutive(player_1_values)
    player_2_is_consecutive = is_consecutive(player_2_values)

    if player_1_is_consecutive and (not player_2_is_consecutive):
        return player_1_wins

    if player_2_is_consecutive and (not player_1_is_consecutive):
        return player_2_wins

    return draw


def flush(player_1, player_2):
    def has_flush(player):
        player_types = player[1]
        first_type = player[1][0]
        for ty in player_types:
            if ty != first_type:
                return False
        return True

    player_1_has_flush = has_flush(player_1)
    player_2_has_flush = has_flush(player_2)

    if player_1_has_flush and (not player_2_has_flush):
        return player_1_wins

    if player_2_has_flush and (not player_1_has_flush):
        return player_2_wins

    return draw


def full_house(player_1, player_2):
    def has_full_house(player):
        player_values = set(player[0])
        if len(player_values) <= 2:
            return True
        return False

    player_1_has_full_house = has_full_house(player_1)
    player_2_has_full_house = has_full_house(player_2)

    if player_1_has_full_house and (not player_2_has_full_house):
        return player_1_wins

    if player_2_has_full_house and (not player_1_has_full_house):
        return player_2_wins

    return draw


def four_of_a_kind(player_1, player_2):
    def has_full_four_of_a_kind(player):
        player_values = set(player[0])
        if len(player_values) > 2:
            return False
        if len(player_values) == 1:
            return True

        # the player has 2 types of values count them
        for val in player_values:
            count = 0
            for num in player[0]:
                if num == val:
                    count += 1
            if count == 4:
                return True
        return False

    player_1_has = has_full_four_of_a_kind(player_1)
    player_2_has = has_full_four_of_a_kind(player_2)

    if player_1_has and (not player_2_has):
        return player_1_wins

    if player_2_has and (not player_1_has):
        return player_2_wins

    return draw

def straight_flush(player_1, player_2):
    def has_flush(player):
        player_types = player[1]
        first_type = player[1][0]
        for ty in player_types:
            if ty != first_type:
                return False
        return True

    def has_straight_flush(player):
        player_values = sorted(player[0])
        player_is_consecutive = is_consecutive(player_values)

        return player_is_consecutive and has_flush(player)

    player_1_has = has_straight_flush(player_1)
    player_2_has = has_straight_flush(player_2)

    if player_1_has and (not player_2_has):
        return player_1_wins

    if player_2_has and (not player_1_has):
        return player_2_wins

    return draw


def royal_flush(player_1, player_2):
    def has_flush(player):
        player_types = player[1]
        first_type = player[1][0]
        for ty in player_types:
            if ty != first_type:
                return False
        return True

    def has_straight_flush(player):
        player_values = sorted(player[0])
        player_is_consecutive = is_consecutive(player_values)

        return player_is_consecutive and has_flush(player)

    def has_royal_flush(player):
        player_values = sorted(player[0])
        return has_straight_flush(player) and min(player_values) == card_value_numeric['T']

    player_1_has = has_royal_flush(player_1)
    player_2_has = has_royal_flush(player_2)

    if player_1_has and (not player_2_has):
        return player_1_wins

    if player_2_has and (not player_1_has):
        return player_2_wins

    return draw

compare_priority = [royal_flush, straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, compare_2_pairs, compare_highest_value_cards]


hands = None

count_player_1_wins = 0
for hand in hands:
    player_1, player_2 = parse_hand_into_2_players(hand)
    for compare_function in compare_priority:
        if compare_function(player_1, player_2) == player_1_wins:
            count_player_1_wins += 1
            break

print(count_player_1_wins)