# if n is even the sum mod a^2 is always 2 (if a > 2)
# because of newton binom
# else it equals 2 * (sum(from k=0 up to n/2) of (n choose 2k) *(a**(n-2*k)))
# which mod a**2 is simply equal to 2*(n choose n-1) * a = 2 * n * a

def calc_r_max_brute(a):
    a_2 = a ** 2

    def calc_r(a, n):
        return ((a - 1) ** n + (a + 1) ** n) % a_2

    max_mod_result = 2  # even n will make r = 2
    for n in range(1, 2*a):
        current_mod_result = calc_r(a,n)
        if current_mod_result > max_mod_result:
            max_mod_result = current_mod_result

    return max_mod_result

def calc_r_max(a):
    """
    :param a:
    :return: works only for a > 2
    """
    a_2 = a ** 2
    max_mod_result = 2  # even n will make r = 2
    for n in range(1, 2*a, 2):
        current_mod_result = (2 * n * a) % a**2
        #print(current_mod_result)
        if current_mod_result > max_mod_result:
            max_mod_result = current_mod_result

    return max_mod_result

summ = 0
for a in range(3, 1001):
    summ += calc_r_max(a)

print(summ)
