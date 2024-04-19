import os
from collections import Counter
from itertools import product
from array import array
from functools import reduce

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        m = int(input())
        s = int(input())
        # dp[x][y][z] = [0, x]까지의 정수 중 y개를 사용해서 합을 z로 만드는 경우의 수
        dp = array("i", [0] * 2 * (n * n + 1) * (s + 1))
        dp[0] = 1
        for x in range(1, m + 1):
            for y in range(n * n + 1):
                for z in range(s + 1):
                    dp[(x & 1) * (n * n + 1) * (s + 1) + y * (s + 1) + z] = dp[((x - 1) & 1) * (n * n + 1) * (s + 1) + y * (s + 1) + z] + (
                        dp[((x - 1) & 1) * (n * n + 1) * (s + 1) + (y - 1) * (s + 1) + z - x] if y >= 1 and 0 <= z - x < s else 0)
                    dp[(x & 1) * (n * n + 1) * (s + 1) + y * (s + 1) + z] %= MOD
        answer = dp[(m & 1) * (n * n + 1) * (s + 1) + n * n * (s + 1) + s]
        answers[h] = f"{answer}"
    print(answers)