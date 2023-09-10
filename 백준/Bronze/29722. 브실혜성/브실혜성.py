# C번 - 브실혜성

y, m, d = map(int, input().split("-"))
n = int(input())
current_day = 360 * y + 30 * m + d
next_day = current_day + n
m, d = divmod(next_day, 30)
y, m = divmod(m, 12)
if d == 0:
    m -= 1
    d += 30
if m == 0:
    y -= 1
    m += 12
print(f"{y:0>4}-{m:0>2}-{d:0>2}")