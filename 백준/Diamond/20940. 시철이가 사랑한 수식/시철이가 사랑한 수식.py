# 20940 시철이가 사랑한 수식


def product_sum(N, MOD):
    return N * (1 + N) * (2 + N) * (1 + 6 * N + 3 * N * N) // 60 % MOD


def square_sum(N, MOD):
    return N * (N + 1) * (2 * N + 1) // 6 % MOD


def cubic_sum(N, MOD):
    return (N * (N + 1)) ** 2 // 4 % MOD


def quartic_sum(N, MOD):
    return N * (N + 1) * (2 * N + 1) * (3 * N * N + 3 * N - 1) // 30 % MOD


def h2_sum(N, l, MOD):
    return (l * square_sum(N // l - 1, MOD) + ((N // l) ** 2) * (1 + N % l)) % MOD


def h3_sum(N, l, MOD):
    return (l * cubic_sum(N // l - 1, MOD) + ((N // l) ** 3) * (1 + N % l)) % MOD


def h4_sum(N, l, MOD):
    return (l * quartic_sum(N // l - 1, MOD) + ((N // l) ** 4) * (1 + N % l)) % MOD


def gcd_sum(N, MOD):
    result = 0
    for i in range(1, N + 1):
        result += phi[i] * h2_sum(N, i, MOD) % MOD
    return result % MOD


def lcm_sum(N, MOD):
    result = 0
    for i in range(1, N + 1):
        result += (
            nu[i]
            * (
                h2_sum(N, i, 4 * MOD)
                + 2 * h3_sum(N, i, 4 * MOD)
                + h4_sum(N, i, 4 * MOD)
            )
            // 4
            % MOD
        )
    return result % MOD


N, K = map(int, input().split(" "))
phi = [i for i in range(1000001)]
nu = [i for i in range(1000001)]
for i in range(2, 1000001):
    if phi[i] != i:
        continue
    j = 1
    while i * j <= 1000000:
        phi[i * j] = phi[i * j] * (i - 1) // i
        nu[i * j] = nu[i * j] * (1 - i)
        j += 1

print(product_sum(N, K))
print(gcd_sum(N, K) * lcm_sum(N, K) % K)