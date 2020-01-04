sum = 100

coins = [i for i in range(1, sum+1)]

ways_to_make = [[0 for j in range(len(coins))] for i in range(sum+1)]
#base case
for i in range(1, sum + 1):
    ways_to_make[i][0] = 1  # there is 1 way to make sum using only ones

for i in range(len(coins)):
    ways_to_make[0][i] = 1  # can write 0 in only 1 way


for j in range(1, len(coins)):
    current_coin = coins[j]
    for i in range(1, sum+1):
        sum_divided_by_coin = i//current_coin
        for k in range(sum_divided_by_coin + 1):
            ways_to_make[i][j] += ways_to_make[i - k*current_coin][j-1]

print(ways_to_make[sum][len(coins)-1] - 1)  # include itself so minus 1
