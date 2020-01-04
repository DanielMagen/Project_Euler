from math import floor, sqrt, ceil

# load words
path = 'C:\\Users\\Daniel\\Desktop\\words.txt'
with open(path) as f:
    words = f.read().split(',')

# remove "
for i in range(len(words)):
    words[i] = words[i][1:len(words[i])-1]


def remove_duplicates_from_sorted_list(lis):
    new_lis = []
    i = 0
    while i < len(lis):
        new_lis.append(lis[i])
        i += 1
        while i < len(lis) and new_lis[-1] == lis[i]:
            i += 1

    return new_lis


def str_to_list(string):
    lis = []
    for c in string:
        lis.append(c)
    return lis

# now create a dictionary for the words
def get_key_of_word(some_word):
    return tuple(sorted(str_to_list(some_word)))

def print_dict(some_dict):
    for key in some_dict:
        print(key, some_dict[key])

words_dic = {}
for word in words:
    word_key = get_key_of_word(word)
    if word_key in words_dic:
        words_dic[word_key].append(word)
    else:
        words_dic[word_key] = [word]

# now remove all words which can not be paired with any other word
new_dic = {}
for key in words_dic:
    if len(words_dic[key]) > 1:
        new_dic[key] = words_dic[key]
words_dic = new_dic

# now turn it into a list of lists of words
similar_words_list = []
for key in words_dic:
    similar_words_list.append(words_dic[key])

# now sort by length of longest word
def get_length_of_longest_word(words_list):
    max_len = 0
    for word in words_list:
        if len(word) > max_len:
            max_len = len(word)
    return max_len

def get_shortest_word_and_its_length_and_rest_of_list(words_list):
    min_word = words_list[0]
    min_len = len(min_word)
    min_i = 0

    for i in range(1, len(words_list)):
        current_word = words_list[i]
        current_len = len(current_word)
        if current_len < min_len:
            min_len = current_len
            min_word = current_word
            min_i = i

    return min_word, min_len, words_list[:min_i] + words_list[min_i+1:]

similar_words_list.sort(key=get_length_of_longest_word, reverse=True) # from biggest to smallest

def find_lowest_and_highest_num_such_that_num_squared_has_x_digits(how_many_digits):
    lowest = int(ceil(sqrt(int('1' + '0'*(how_many_digits-1)))))
    highest = int(floor(sqrt(int('9'*how_many_digits))))
    return lowest, highest


# now go through the similar_words_list and try to find a mapping that makes a pair of squares

def get_map_of_word_to_digits(word, num):
    """
    if there is no valid map it returns none
    it assumes that the word and number has the same length
    """
    word_char_list = str_to_list(word)
    num_digit_list = str_to_list(str(num))
    word_to_digits = {}
    digits_to_word = {}

    for i in range(len(word_char_list)):
        current_char = word_char_list[i]
        current_digit = num_digit_list[i]
        if current_char in word_to_digits:
            if word_to_digits[current_char] != current_digit:
                return None
        else:
            if current_digit in digits_to_word:
                return None

            word_to_digits[current_char] = current_digit
            digits_to_word[current_digit] = current_char

    return word_to_digits

def apply_word_to_digit_map_to_number(word_to_digit_map, word):
    """
    if the resulting number has a leading zero it returns none
    """
    if word_to_digit_map[word[0]] == '0':
        return None
    new_number = ''
    for c in word:
        new_number += word_to_digit_map[c]

    return int(new_number)

def is_square(num):
    return (sqrt(num) % 1) == 0


max_word_number = 0
max_word_number_word = ''
max_word_number_word_initial = ''
max_word_number_word_initial_number = 0

for words_list in similar_words_list:
    min_word, digit_length, rest_of_words = get_shortest_word_and_its_length_and_rest_of_list(words_list)
    lowest, highest = find_lowest_and_highest_num_such_that_num_squared_has_x_digits(digit_length)

    for i in range(lowest, highest + 1):
        current_square = i**2
        word_to_digit_map = get_map_of_word_to_digits(min_word, current_square)
        if word_to_digit_map is None:
            continue

        for word in rest_of_words:
            word_number = apply_word_to_digit_map_to_number(word_to_digit_map, word)
            if word_number is None:
                continue
            if is_square(word_number):
                if max_word_number < word_number:
                    max_word_number = word_number
                    max_word_number_word = word
                    max_word_number_word_initial = min_word
                    max_word_number_word_initial_number = current_square

print(max_word_number)
print(max_word_number_word)
print(max_word_number_word_initial)
print(max_word_number_word_initial_number)