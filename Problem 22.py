names = "-----------copy names here-----------"
names.sort()


def score_name(name):
    if len(name) == 1:
        return ord(name) - 64
    return ord(name[-1]) - 64 + score_name(name[:-1])

summ = 0
for i in range(len(names)):
    summ += score_name(names[i]) * (i+1)
print(summ)