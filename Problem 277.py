def reverse_D(a_n1):
    a_n = 3 * a_n1
    return a_n

def reverse_U(a_n1):
    a_n = (3 * a_n1 - 2) / 4
    return a_n


def reverse_d(a_n1):
    a_n = (3 * a_n1 + 1) / 2
    return a_n

def get_reverse_function(rev_operation_sequence, starting_number):
    current = starting_number
    for c in rev_operation_sequence:
        if c == 'D':
            current = reverse_D(current)

        elif c == 'U':
            current = reverse_U(current)

        elif c == 'd':
            current = reverse_d(current)

        else:
            #print('unsupported operation', c)
            return None
        
    return current

"""
from sympy import Symbol

operation_sequence = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
rev_operation_sequence = reversed(operation_sequence)

x = Symbol('x')
f = x
f = get_reverse_function(rev_operation_sequence,f)
print(f)


#  from this I learned that the function is 205891132094649*x/4194304 + 21110037246199/4194304
# so the question is when 205891132094649*x + 21110037246199 is divisible by 4194304
so when 205891132094649*x + 21110037246199 = 0 mod 4194304

205891132094649 % 4194304 = 686265
21110037246199 % 4194304 = 356599

so the question is when 
686265*x + 356599 = 0 mod 4194304

686265*x = 3837705 mod 4194304

686265 Modular multiplicative inverse (mod 4194304) = 2362761
so 
2362761*686265*x = 2362761*3837705 mod 4194304
x = 1966289 mod 4194304
so x = 1966289 + 4194304*k
"""

# from wiki books
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



bigger_than = 10**15

overall_function = lambda x: (205891132094649*x + 21110037246199)/4194304

start = 1966289
for k in range(10):
    result = overall_function(start)
    if result > bigger_than:
        print(result)
        break
    start += 4194304