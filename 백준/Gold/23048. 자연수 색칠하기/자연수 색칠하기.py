# 23048 자연수 색칠하기


def color_number(limit: int) -> tuple[int, list[int]]:
    prime_color = [0, 1] + [0 for _ in range(2, limit + 1)]
    color_count = 1
    for i in range(2, limit + 1):
        if prime_color[i]:
            continue
        color_count += 1
        prime_color[i : limit + 1 : i] = [color_count] * (limit // i)
    return color_count, prime_color


N = int(input())
color_count, prime_color = color_number(N)
print(color_count)
print(*prime_color[1:])