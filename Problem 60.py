def prime_list(up_to):
    prime_mark = 1
    natural_list = [prime_mark for i in range(up_to)]
    for i in range(2, int(len(natural_list)**0.5) + 1):
        if natural_list[i] == 0:
            continue
        for j in range(i**2, len(natural_list), i):
            natural_list[j] = 0

    list_of_primes = []
    for i in range(2, len(natural_list)):
        if natural_list[i] == prime_mark:
            list_of_primes.append(i)

    return list_of_primes

class combo:
    def __init__(self, num):
        self.number_set = set([num])

    def size(self):
        return len(self.number_set)

    def is_in(self, num):
        return num in self.number_set

    def join(self, other_combo):
        self.number_set += other_combo.number_set

def get_concatenations(lis, num):
    """
    :param lis:
    :param num:
    :return: all the possible combinations of the num with the numbers in the list
    """
    num = str(num)
    combos = []
    for item in lis:
        item_str = str(item)
        combos.append(int(item_str + num))
        combos.append(int(num + item_str))
    return combos

def get_all_partitions(num):
    num = str(num)
    partitions = []
    for i in range(1, len(num)):
        partitions.append([int(num[:i]), int(num[i:])])

    return partitions

def join_nums(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    return int(num1+num2)


primes = prime_list(10000000)
primes_set = set(primes)

# create sets of 2 primes
primes_2 = [None for i in range(len(primes))]
can_skip = set([])
for p in primes:
    if p < 10 or p in can_skip:
        continue
    p_partitions = get_all_partitions(p)
    for par in p_partitions:
        joined1 = join_nums(par[1], par[0])
        joined2 = join_nums(par[0], par[1])
        if par[0] in primes_set and par[1] in primes_set and joined2 in primes_set and joined1 in primes_set:
            par_0_place = primes.index(par[0])
            par_1_place = primes.index(par[1])

            if primes_2[par_0_place] is None:
                primes_2[par_0_place] = []

            if primes_2[par_1_place] is None:
                primes_2[par_1_place] = []

            par_set = set(par)
            if par_set not in primes_2[par_0_place]:
                primes_2[par_0_place].append(par_set)

            if par_set not in primes_2[par_1_place]:
                primes_2[par_1_place].append(par_set)
            can_skip.add(joined1)
            can_skip.add(joined2)

all_sets_of_2 = []
for combos in primes_2:
    if combos is not None:
            for comb in combos:
                comb = sorted(list(comb))
                if comb not in all_sets_of_2:
                    all_sets_of_2.append(comb)

all_sets_of_2 = sorted(all_sets_of_2)
print(all_sets_of_2)

max_starting_number = 0
for par in all_sets_of_2:
    if par[0] > max_starting_number:
        max_starting_number = par[0]

all_groups = [[] for i in range(max_starting_number +1)]

for par in all_sets_of_2:
    all_groups[par[0]].append(par)

def find_all_cliques_of_size(size_of_clique, starting_number):
    if starting_number >= len(all_groups):
        return []
    if size_of_clique == 2:
        return all_groups[starting_number]

    all_cliques = []
    all_groups_that_include_starting_number = all_groups[starting_number]

    for par_of_size_2_with_starting_number in all_groups_that_include_starting_number:
        for number in par_of_size_2_with_starting_number:
            if number != starting_number:
                all_cliques_of_other_number = find_all_cliques_of_size(size_of_clique - 1, number)
                for clique in all_cliques_of_other_number:
                    to_add_to_my_cliques = True
                    for number_in_clique in clique:
                        if sorted([starting_number, number_in_clique]) not in all_sets_of_2:
                            to_add_to_my_cliques = False
                            break
                    if to_add_to_my_cliques:
                        all_cliques.append(clique + [starting_number])
    return all_cliques


starting_numbers = set([])
for par in all_sets_of_2:
    starting_numbers.add(par[0])

all_5s = []
for num in starting_numbers:
    all_5s += find_all_cliques_of_size(5,num)

min_sum = 10000000
min_lis = []
for lis in all_5s:
    summ = sum(lis)
    if summ < min_sum:
        min_sum = summ
        min_lis = lis
print(min_sum)
print(min_lis)

