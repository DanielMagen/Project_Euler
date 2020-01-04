special = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}

def spell_number(num):
    if num == 100 or num == 1000:
        return "one " + special[num]
    if num in special:
        return special[num]
    spelling = ""
    if num > 100:
        spelling += special[num//100] + " "+ special[100]
        num = num % 100
        if 0 < num:
            spelling += " and "

    if num > 20:
        spelling += special[(num // 10) *10] + " "
        num = num % 10

    if num != 0:
        spelling += special[num]

    return spelling

def count_letters(string):
    count = 0
    for i in range(len(string)):
        if string[i] != ' ':
            count += 1
    return count

total_sum = 0
for i in range(1,1001):
    print(spell_number(i))
    total_sum += count_letters(spell_number(i))

print(total_sum)



