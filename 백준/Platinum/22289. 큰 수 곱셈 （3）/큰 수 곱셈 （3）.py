# 22289 큰 수 곱셈 (3)

from math import ceil, log2, cos, sin
from cmath import pi

MOD = 2013265921
ROOT = 31


def ntt(a, invert: bool):
    N = len(a)
    bit_reverse_permutation(a, N)
    m = 1
    step = MOD - 1
    for _ in range(1, int(log2(N)) + 1):
        m <<= 1
        step >>= 1
        angle = pow(ROOT, step, MOD)
        if invert:
            angle = pow(angle, -1, MOD)
        for k in range(0, N, m):
            w = 1
            for j in range(k, k + (m >> 1)):
                t = w * a[j + (m >> 1)] % MOD
                u = a[j]
                a[j] = u + t
                a[j + (m >> 1)] = u - t
                w = w * angle % MOD
                if a[j] >= MOD:
                    a[j] -= MOD
                if a[j + (m >> 1)] < 0:
                    a[j + (m >> 1)] += MOD
    if invert:
        inv_N = pow(N, -1, MOD)
        for i, v in enumerate(a):
            a[i] = v * inv_N % MOD


def bit_reverse_permutation(a, N):
    j = 0
    for i in range(1, N):
        bit = N >> 1
        while not ((j := j ^ bit) & bit):
            bit >>= 1
        if i < j:
            a[i], a[j] = a[j], a[i]


def polynomial_multiplication(a, b):
    original_size = len(a) + len(b) - 1
    degree = ceil(log2(original_size))
    size = 1 << degree
    a_padded = a + [0] * (size - len(a))
    b_padded = b + [0] * (size - len(b))
    ntt(a_padded, False)
    ntt(b_padded, False)
    for i, v in enumerate(b_padded):
        a_padded[i] *= v
        a_padded[i] %= MOD
    ntt(a_padded, True)
    result = [x for i, x in enumerate(a_padded) if i < original_size]
    for i, v in enumerate(result):
        if i + 1 == len(result):
            break
        if v < 10:
            continue
        result[i + 1] += v // 10
        result[i] = v % 10
    if len(result) != 1 and result[-1] == 0:
        result.pop()
    return result


a_str, b_str = input().strip().split(" ")
a = list(map(int, reversed(list(a_str))))
b = list(map(int, reversed(list(b_str))))
result = polynomial_multiplication(a, b)
result.reverse()
print(*result, sep="")