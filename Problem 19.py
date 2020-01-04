def month_to_days(month, year):
    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                return 28
            return 29
        return 28

    if month in [9, 4, 6, 11]:
        return 30
    return 31

def get_next_month(current_month):
    if current_month + 1 == 13:
        return 1
    return current_month + 1

def get_next_day(current_day, increase_by):
    current_day += increase_by
    current_day = current_day % 7
    return current_day



current_year = 1901
current_month = 1
current_day = 2

sundays_count = 0

while current_year < 2001:
    month_days = month_to_days(current_month, current_year)

    current_month = get_next_month(current_month)

    if current_month == 1:
        current_year += 1

    print("current day is",current_day+1)
    print("adding days:",month_days)
    current_day = get_next_day(current_day, month_days)
    print("now day is", current_day+1)
    print()

    if current_day == 0:
        sundays_count += 1

print(sundays_count)
