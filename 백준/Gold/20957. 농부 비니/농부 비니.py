# 20957 농부 비니

from itertools import product
import os
from array import array


def main():
    tokens = iter(os.read(0, os.fstat(0).st_size).split())
    MOD = 10**9 + 7
    dp = array("I", [0 for _ in range(490000)])
    for i in range(10000):
        for j in range(10):
            if i == 0 and j == 0:
                continue
            if i == 0:
                dp[(j % 7) * 7 + j % 7] += 1
                continue
            for a, b in product(range(7), repeat=2):
                dp[i * 49 + ((a + j) % 7) * 7 + (b * j) % 7] += dp[
                    (i - 1) * 49 + a * 7 + b
                ]
                dp[i * 49 + ((a + j) % 7) * 7 + (b * j) % 7] %= MOD
    T = int(next(tokens))
    os.write(
        1,
        "\n".join(
            map(str, [dp[int(next(tokens)) * 49 - 49] for _ in range(T)])
        ).encode(),
    )
    os._exit(0)


main()