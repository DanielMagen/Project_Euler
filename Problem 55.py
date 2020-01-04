def is_palindromic(num):
    num = str(num)
    rev_num = num[::-1]
    return rev_num == num

def get_reverse_num(num):
    return int(str(num)[::-1])

def is_lychrel(num):
    for i in range(50):
        num = num + get_reverse_num(num)
        if is_palindromic(num):
            return False
    return True


count = 0
for i in range(10000):
    if is_lychrel(i):
        count += 1
print(count)
