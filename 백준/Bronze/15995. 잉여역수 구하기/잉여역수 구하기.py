# 15995 잉여역수 구하기


def eea(a: int, b: int, d: int) -> int:
    # (x(0),y(0)) = (1,0), (x(1),y(1)) = (0,1)
    x_y_seq_memo: list[list[int]] = [[1, 0], [0, 1]]
    # r(0) = a, r(1) = b
    r_memo: list[int] = [a, b]
    q_i: int = 0
    i: int = 2
    while True:
        # q(i+2) = r(i)//r(i+1)
        q_i = r_memo[(i - 2) % 2] // r_memo[(i - 1) % 2]
        # r(i+2) = r(i)//r(i+1)
        r_memo[i % 2] = r_memo[(i - 2) % 2] % r_memo[(i - 1) % 2]
        # (x(i+2),y(i+2))=(x(i)-x(i+1)*q(i+2),y(i)-y(i+1)*q(i+2))
        for j in range(2):
            x_y_seq_memo[i % 2][j] = (
                x_y_seq_memo[(i - 2) % 2][j] - x_y_seq_memo[(i - 1) % 2][j] * q_i
            )
        if r_memo[i % 2] == d:
            break
        else:
            i += 1
    return x_y_seq_memo[i % 2][0]


a, m = map(int, input().split(" "))
print(eea(a, m, 1) % m)