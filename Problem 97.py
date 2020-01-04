upto = 7830457

def get_last_digits(num, how_many_digits):
    num = str(num)
    return int(num[-how_many_digits:])

curr = 1
for i in range(upto):
    curr = get_last_digits(curr*2, 10)

print(get_last_digits((curr * 28433) + 1, 10))