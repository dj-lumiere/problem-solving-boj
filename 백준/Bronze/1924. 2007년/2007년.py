# 1924 2007년

from datetime import date

x, y = map(int, input().split(" "))
a = date(2007, x, y)
day_of_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
print(day_of_week[a.weekday()])