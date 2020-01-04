def prime_list(up_to):
    natrual_list = [1 for i in range(up_to)]
    for i in range(2, int(len(natrual_list)**0.5) + 1):
        if natrual_list[i] == 0:
            continue
        for j in range(i**2, len(natrual_list), i):
            natrual_list[j] = 0

    list_of_primes = []
    for i in range(2, len(natrual_list)):
        if(natrual_list[i] == 1):
            list_of_primes.append(i)

    return list_of_primes

coins = prime_list(100)

sum = 71  # experiment until got to this number
ways_to_make = [[0 for j in range(len(coins))] for i in range(sum+1)]
#base case
for i in range(2, sum + 1, 2):
    ways_to_make[i][0] = 1  # there is 1 way to make even sum using only twos

for i in range(len(coins)):
    ways_to_make[0][i] = 1  # there is 1 way to make 0

for j in range(1, len(coins)):
    current_coin = coins[j]
    for i in range(1, sum+1):
        sum_divided_by_coin = i//current_coin
        for k in range(sum_divided_by_coin + 1):
            ways_to_make[i][j] += ways_to_make[i - k*current_coin][j-1]


print(ways_to_make[sum][len(coins)-1])