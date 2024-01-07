# 10504 덧셈


def find_continuous_sum(n):
    for i in range(2, int((2 * n) ** 0.5) + 1, 1):
        start, remainder = divmod((n - i * (i + 1) // 2), i)
        if remainder != 0:
            continue
        return tuple(range(start + 1, start + 1 + i))
    return ()


T = int(input())
for _ in range(T):
    n = int(input())
    result = find_continuous_sum(n)
    if not result:
        print("IMPOSSIBLE")
    else:
        print(f"{n} = ", end="")
        print(*result, sep=" + ")
