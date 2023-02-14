# 3955 캔디 분배

# kx+1 = ac인 a가 존재?
# kx === -1 (mod c)


def eea(a: int, b: int, d: int) -> list[int]:
    x_y_seq_memo: list[list[int]] = [[1, 0], [0, 1]]
    r_memo: list[int] = [a, b]
    q_i: int = 0
    i: int = 2
    while True:
        q_i = r_memo[(i - 2) % 2] // r_memo[(i - 1) % 2]
        r_memo[i % 2] = r_memo[(i - 2) % 2] - r_memo[(i - 1) % 2] * q_i
        for j in range(2):
            x_y_seq_memo[i % 2][j] = (
                x_y_seq_memo[(i - 2) % 2][j] - x_y_seq_memo[(i - 1) % 2][j] * q_i
            )
        if r_memo[i % 2] == d:
            break
        else:
            i += 1
    return x_y_seq_memo[i % 2]


def gcd(x, y) -> int:
    if x < y:
        x, y = y, x
    if x % y:
        return gcd(y, x % y)
    else:
        return y


T = int(input())
for _ in range(T):
    k, c = list(map(int, input().split(" ")))
    if gcd(k, c) != 1:
        print("IMPOSSIBLE")
    elif c == 1 and k == 10**9:
        print("IMPOSSIBLE")
    elif c == 1 and k < 10**9:
        print(k + 1)
    elif k == 1:
        print(1)
    else:
        a, x = eea(c, k, 1)
        if a <= 0:
            n = x // c + 1
            a += n * k
            x = x % c
        if a > 10**9:
            print("IMPOSSIBLE")
        else:
            print(a)
