# 27172 수 나누기 게임

N = int(input())
x = [int(value) for value in input().split(" ")]
check_value_max = max(x)
score = [0 for i in range(check_value_max + 1)]
has_appeared = [False for i in range(check_value_max + 1)]
for value in x:
    has_appeared[value] = True
for value in x:
    next_value = value * 2
    while next_value <= check_value_max:
        if has_appeared[next_value]:
            score[value] += 1
            score[next_value] -= 1
        next_value += value
print(*[score[value] for value in x])