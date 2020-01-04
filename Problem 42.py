names = "-----------copy names here-----------"

def score_name(name):
    if len(name) == 1:
        return ord(name) - 64
    return ord(name[-1]) - 64 + score_name(name[:-1])


def get_first_n_triangle_numbers(n):
    return [i*(i+1)/2 for i in range(1,n+1)]

triangles = set(get_first_n_triangle_numbers(200))
count = 0
for name in names:
    if score_name(name) in triangles:
        count += 1
print(count)