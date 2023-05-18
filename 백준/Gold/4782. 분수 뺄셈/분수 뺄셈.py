# 4782 분수 뺄셈
# an**2+bm**2=2bmn
# b와 n 주어짐, a와 m 구하기
from fractions import Fraction

while True:
    b, n = list(map(int, input().split(" ")))
    if b == n == 0:
        break
    else:
        answer_list: list[tuple] = []
        for m in range(2 * n, 0, -1):
            if m == n:
                continue
            if not b * m * (2 * n - m) % n**2:
                answer_list.append((b * m * (2 * n - m) // n**2, m))
        answer_list = sorted(answer_list, key=lambda x: (Fraction(x[0], x[1]), x[0]))
        print(*[f"{i}/{j}" for i, j in answer_list])