upto = 9000
cubes = [i**3 for i in range(1,upto)]

def list_to_str(lis):
    s = ""
    for item in lis:
        s += item
    return s

def sort_num(num):
    num = str(num)
    lis = []
    for i in range(len(num)):
        lis.append(num[i])
    lis = sorted(lis)
    return list_to_str(lis)


for i in range(len(cubes)):
    cubes[i] = sort_num(cubes[i])

appearances = {}
for i in range(len(cubes)):
    if cubes[i] in appearances:
        appearances[cubes[i]] += 1
    else:
        appearances[cubes[i]] = 1

search_for = 5
found = 0
for number in appearances:
    if appearances[number] == search_for:
        found = number
        print(found)
        print("")


for i in range(len(cubes)):
    if cubes[i] == found:
        print((i+1)**3)



