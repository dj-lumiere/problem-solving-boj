# 1568 새

N = int(input())
answer = 0
current_streak = 1
while N >= 0:
    if N < current_streak:
        answer += current_streak - 1
        current_streak = 1
        if N == 0:
            break
        else:
            continue
    N -= current_streak
    current_streak += 1
print(answer)