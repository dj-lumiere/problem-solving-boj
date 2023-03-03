# 3009 네 번째 점
from collections import Counter

x_values: list[int] = []
y_values: list[int] = []

for _ in range(3):
    x, y = list(map(int, input().split(" ")))
    x_values.append(x)
    y_values.append(y)

x_values_counter: Counter[int] = Counter(x_values)
y_values_counter: Counter[int] = Counter(y_values)
x_answer: int = 0
y_answer: int = 0

for i, j in x_values_counter.items():
    if j == 1:
        x_answer = i

for i, j in y_values_counter.items():
    if j == 1:
        y_answer = i
print(x_answer, y_answer)