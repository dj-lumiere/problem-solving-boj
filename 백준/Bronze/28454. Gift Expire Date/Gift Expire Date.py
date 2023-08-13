# 28454 Gift Expire Date
from datetime import date, timedelta

y, m, d = map(int, input().split("-"))
current_time = date(y, m, d)
answer = 0
N = int(input())
for _ in range(N):
    y, m, d = map(int, input().split("-"))
    gifticon_due_date = date(y, m, d)
    if gifticon_due_date - current_time >= timedelta(0):
        answer += 1
print(answer)