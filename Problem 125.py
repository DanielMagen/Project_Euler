def is_palindromic(num):
    num = str(num)
    rev_num = num[::-1]
    return rev_num == num

up_to = 10**8
squares = [i**2 for i in range(int(up_to**0.5) + 1)]
squares_sum = squares.copy()
all_palindromes = set([])

current_iteration = 0

current_iteration += 1
for i in range(1, min(len(squares_sum), len(squares) - current_iteration)):
    squares_sum[i] += squares[i + current_iteration]
    if squares_sum[i] > up_to:
        squares_sum = squares_sum[:i]
        break

while True:
    for num in squares_sum:
        if is_palindromic(num):
            all_palindromes.add(num)

    current_iteration += 1
    for i in range(1, min(len(squares_sum), len(squares)-current_iteration)):
        squares_sum[i] += squares[i+current_iteration]
        if squares_sum[i] > up_to:
            squares_sum = squares_sum[:i]
            break

    if len(squares_sum) < 2:
        break

print(sum(all_palindromes))