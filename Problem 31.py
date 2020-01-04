coins = [1,2,5,10,20,50,100,200]

sum = 200
ways_to_make = [[0 for j in range(len(coins))] for i in range(sum+1)]
#base case
for i in range(1, sum + 1):
    ways_to_make[i][0] = 1  # there is 1 way to make sum using only ones

for i in range(len(coins)):
    ways_to_make[0][i] = 1  # there is 1 way to make 0

for j in range(1, len(coins)):
    current_coin = coins[j]
    for i in range(1, sum+1):
        sum_divided_by_coin = i//current_coin
        for k in range(sum_divided_by_coin + 1):
            ways_to_make[i][j] += ways_to_make[i - k*current_coin][j-1]



print(ways_to_make[sum][len(coins)-1])