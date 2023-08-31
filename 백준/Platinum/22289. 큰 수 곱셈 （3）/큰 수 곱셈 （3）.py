# 22289 큰 수 곱셈 (3)

from math import ceil, log2
from sys import stdout


def print(target: str):
    stdout.write(target)


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
                a[j] = (u + t) % MOD
                a[j + (m >> 1)] = (u - t) % MOD
                w = w * angle % MOD
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


def ntt(a, invert: bool, MOD, ROOT):
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
    MOD1 = 2013265921
    ROOT1 = 31
    MOD2 = 2113929217
    ROOT2 = 5
    MOD1_MULINV = 21
    MOD2_MULINV = 2013265901
    original_size = len(a) + len(b) - 1
    degree = ceil(log2(original_size))
    size = 1 << degree
    a_padded1 = a + [0] * (size - len(a))
    b_padded1 = b + [0] * (size - len(b))
    a_padded2 = a + [0] * (size - len(a))
    b_padded2 = b + [0] * (size - len(b))
    ntt(a_padded1, False, MOD1, ROOT1)
    ntt(b_padded1, False, MOD1, ROOT1)
    ntt(a_padded2, False, MOD2, ROOT2)
    ntt(b_padded2, False, MOD2, ROOT2)
    for i, v in enumerate(b_padded1):
        a_padded1[i] *= v
        a_padded1[i] %= MOD1
    for i, v in enumerate(b_padded2):
        a_padded2[i] *= v
        a_padded2[i] %= MOD2
    ntt(a_padded1, True, MOD1, ROOT1)
    ntt(a_padded2, True, MOD2, ROOT2)
    result = [
        (v1 * MOD2 * MOD2_MULINV + v2 * MOD1 * MOD1_MULINV) % (MOD1 * MOD2)
        for i, (v1, v2) in enumerate(zip(a_padded1, a_padded2))
        if i < original_size
    ]
    for i, v in enumerate(result):
        if i + 1 >= len(result):
            continue
        result[i + 1] += result[i] // (10**6)
        result[i] %= 10**6
    if len(result) != 1 and result[-1] == 0:
        result.pop()
    result.reverse()
    for i, v in enumerate(result):
        if i == 0:
            print(f"{v}")
            continue
        print(f"{v:0>6}")


a_str, b_str = input().strip().split(" ")
a = [0] * ceil(len(a_str) / 6)
b = [0] * ceil(len(b_str) / 6)
for i in range(len(a)):
    if i == 0:
        a[i] = int(a_str[-6 * i - 6 :])
        continue
    a[i] = int(a_str[-6 * i - 6 : -6 * i])
for i in range(len(b)):
    if i == 0:
        b[i] = int(b_str[-6 * i - 6 :])
        continue
    b[i] = int(b_str[-6 * i - 6 : -6 * i])
polynomial_multiplication(a, b)