def cond(num):
    num_squared = str(num**2)
    if len(num_squared) != 19:
        return False
    for i in range(9):
        if num_squared[2*i] != str(i+1)[-1]:
            return False
    return True

iter = 1
for i in range(10**9, 10**10, 10):
    iter += 1
    if iter% 1000000 == 0:
        print('current iter', iter)
    if cond(i):
        print('found         ----', i)

print("finished")
