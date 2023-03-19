# 10327 피보나치 문제해결전략

from bisect import bisect_left
from math import gcd, ceil, floor

fib = [1, 0, 1, 1]
while True:
    fib_prev_prev, fib_prev = fib[-2], fib[-1]
    fib_next = fib_prev_prev + fib_prev
    if fib_next > 10**9:
        break
    else:
        fib.append(fib_next)


def eea(a: int, b: int, d: int) -> list[int]:
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
        r_memo[i % 2] = r_memo[(i - 2) % 2] - q_i * r_memo[(i - 1) % 2]
        # (x(i+2),y(i+2))=(x(i)-x(i+1)*q(i+2),y(i)-y(i+1)*q(i+2))
        for j in range(2):
            x_y_seq_memo[i % 2][j] = (
                x_y_seq_memo[(i - 2) % 2][j] - x_y_seq_memo[(i - 1) % 2][j] * q_i
            )
        if r_memo[i % 2] == d:
            break
        else:
            i += 1
    return x_y_seq_memo[i % 2]


T: int = int(input())
for _ in range(T):
    n: int = int(input())
    index: int = bisect_left(fib, n)
    if n == 4:
        print(2, 2)
    elif n <= 3:
        print(1, 1)
    else:
        solution: list[tuple[int, int]] = []
        for i in range(index, 5 - 1, -1):
            a: int = fib[i - 2]
            b: int = fib[i - 1]
            d: int = gcd(a, b)
            a, b = a // d, b // d
            if not (n % d):
                x, y = eea(a, b, 1)
                x, y = x * n // d, y * n // d
                if x < 0:
                    k = ceil(x / -b)
                    x, y = x + b * k, y - a * k
                elif y < 0:
                    k = ceil(y / -a)
                    x, y = x - b * k, y + a * k
                if x >= 0 and y >= 0 and x > y:
                    j: int = ceil((x - y) / (a + b))
                    x_new, y_new = x - b * j, y + a * j
                    if x_new <= y_new and x_new > 0:
                        solution.append((x_new, y_new))
                elif x >= 0 and y >= 0 and x <= y:
                    j: int = floor((y - x) / (a + b))
                    x_new, y_new = x + b * j, y - a * j
                    if x_new <= y_new and x_new > 0:
                        solution.append((x_new, y_new))
        if solution:
            solution = sorted(solution, key=lambda x: (x[1], x[0]))
            print(*solution[0])
            solution.clear()