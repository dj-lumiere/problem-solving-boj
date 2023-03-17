# 5430 AC

from collections import deque

T = int(input())
for _ in range(T):
    p: list[str] = list(input())
    n: int = int(input())
    if n:
        x: deque[int] = deque(map(int, input().lstrip("[").rstrip("]").split(",")))
    else:
        _waste = input().lstrip("[").rstrip("]").split(",")
        x: deque[int] = deque()
    pop_from_left_indicator = True
    reverse_indicator = False
    error_indicator = False
    for operators in p:
        if operators == "R":
            pop_from_left_indicator = not pop_from_left_indicator
            reverse_indicator = not reverse_indicator
        elif operators == "D" and not n:
            error_indicator = True
            break
        elif operators == "D" and n and pop_from_left_indicator:
            x.popleft()
            n -= 1
        elif operators == "D" and n and not pop_from_left_indicator:
            x.pop()
            n -= 1
    if error_indicator:
        print("error")
    elif reverse_indicator:
        new_x = list(x)[::-1]
        print("[", end="")
        print(*new_x, sep=",", end="")
        print("]")
    else:
        print("[", end="")
        print(*x, sep=",", end="")
        print("]")
