from math import sqrt

def get_blue(red):
    det = sqrt(1+8*(red**2))

    a = 1 + 2*red

    return (a + det) / 2


def get_red(blue):
    det = sqrt(8*(blue**2) - 8*blue +1)

    a = 1 - 2 * blue

    return (a + det) / 2


def get_valid_r():
    two_previous_a = [2, 5]
    two_previous_b = [3, 7]

    while True:
        next_a = (two_previous_a[1] * 2) + two_previous_a[0]
        next_b = (two_previous_b[1] * 2) + two_previous_b[0]
        two_previous_a = [two_previous_a[1], next_a]
        two_previous_b = [two_previous_b[1], next_b]
        yield next_a * next_b


up_to = 10**12
gen = get_valid_r()
for red in gen:
    blue = get_blue(red)
    if blue + red > up_to:
        print(blue)
        break

