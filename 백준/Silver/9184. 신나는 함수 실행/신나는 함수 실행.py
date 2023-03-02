# 9184 신나는 함수 실행

w_list: list[list[list[int]]] = [
    [[1 for a in range(20 + 1)] for b in range(20 + 1)] for c in range(20 + 1)
]

for a in range(1, 20 + 1):
    for b in range(1, 20 + 1):
        for c in range(1, 20 + 1):
            if a < b < c:
                w_list[c][b][a] = (
                    w_list[c - 1][b][a] + w_list[c - 1][b - 1][a] - w_list[c][b - 1][a]
                )
            else:
                w_list[c][b][a] = (
                    w_list[c][b][a - 1]
                    + w_list[c][b - 1][a - 1]
                    + w_list[c - 1][b][a - 1]
                    - w_list[c - 1][b - 1][a - 1]
                )


def w(a: int, b: int, c: int) -> int:
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a>20 or b>20 or c>20:
        return w_list[20][20][20]
    else:
        return w_list[c][b][a]


while True:
    a, b, c = list(map(int, input().split(" ")))
    if a == b == c == -1:
        break
    else:
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
