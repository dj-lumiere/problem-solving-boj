from fractions import Fraction
 
MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS

 
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(year, month):
    if is_leap_year(year) and month == 2:
        return 29
    month_table = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_table[month]


def to_seconds(y, m, d, h, minute, s):
    total_seconds = 0
    leap_year_count = (y - 1) // 4 - (y - 1) // 100 + (y - 1) // 400
    total_seconds += (365 * (y - 1) + leap_year_count) * DAY_SECONDS
    for month in range(1, m):
        total_seconds += days_in_month(y, month) * DAY_SECONDS
    total_seconds += (d - 1) * DAY_SECONDS
    total_seconds += h * HOUR_SECONDS
    total_seconds += minute * MINUTE_SECONDS
    total_seconds += s
    return total_seconds


def fraction_in_month(y, m, d, h, minute, s):
    total_seconds = 0
    total_seconds += (d - 1) * DAY_SECONDS
    total_seconds += h * HOUR_SECONDS
    total_seconds += minute * MINUTE_SECONDS
    total_seconds += s
    return Fraction(total_seconds, days_in_month(y, m) * DAY_SECONDS)


def fraction_in_year(y, m, d, h, minute, s):
    total_seconds = 0
    for month in range(1, m):
        total_seconds += days_in_month(y, month) * DAY_SECONDS
    total_seconds += (d - 1) * DAY_SECONDS
    total_seconds += h * HOUR_SECONDS
    total_seconds += minute * MINUTE_SECONDS
    total_seconds += s
    return Fraction(total_seconds, (365 + is_leap_year(y)) * DAY_SECONDS)


def sol():
    a1, a2, a3, a4, a5, a6 = map(int, input().split())
    b1, b2, b3, b4, b5, b6 = map(int, input().split())
    unit = input()

    birth_total_seconds = to_seconds(a1, a2, a3, a4, a5, a6)
    cur_total_seconds = to_seconds(b1, b2, b3, b4, b5, b6)

    diff_seconds = cur_total_seconds - birth_total_seconds

    if unit == "Year":
        current_fraction = fraction_in_year(b1, b2, b3, b4, b5, b6)
        birth_fraction = fraction_in_year(a1, a2, a3, a4, a5, a6)
        is_full_year = 1 if current_fraction >= birth_fraction else 0
        print(b1 - a1 - 1 + is_full_year)
    elif unit == "Month":
        current_fraction = fraction_in_month(b1, b2, b3, b4, b5, b6)
        birth_fraction = fraction_in_month(a1, a2, a3, a4, a5, a6)
        is_full_month = 1 if current_fraction >= birth_fraction else 0
        print((b1 - a1) * 12 + b2 - a2 - 1 + is_full_month)
    elif unit == "Day":
        print(diff_seconds // DAY_SECONDS)


T = int(input())
for _ in range(T):
    sol()
