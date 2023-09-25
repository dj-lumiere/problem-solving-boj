# 11691 LCM(i, j)

from sys import stdin


def input():
    return stdin.readline().strip()


PRECOMPUTE_LIMIT = 100000
MOD = 10**9 + 7
phi = [i for i in range(1000001)]
for i in range(2, 1000001):
    if phi[i] != i:
        continue
    j = 1
    while i * j <= 1000000:
        phi[i * j] = phi[i * j] * (i - 1) // i
        j += 1
N = int(input())
n_over_d_possible_values = []
for i in range(1, int(N**0.5) + 1):
    if i == N // i:
        n_over_d_possible_values.append(i)
    else:
        n_over_d_possible_values.extend([i, N // i])
n_over_d_possible_values.sort()
n_over_d_lower_limit = [N // i for i in n_over_d_possible_values]
i_square_phi_i_acc_sum = [0, 0]
for i in range(2, 1000001):
    i_square_phi_i_acc_sum.append(
        (i_square_phi_i_acc_sum[-1] + i * i * phi[i] // 2) % MOD
    )
result = 0
n_over_d_as_gcd_sum = []
for i, v in enumerate(n_over_d_lower_limit):
    if i == 0:
        n_over_d_as_gcd_sum.append(
            (
                (n_over_d_possible_values[i])
                * (n_over_d_possible_values[i] + 1)
                // 2
                * i_square_phi_i_acc_sum[n_over_d_lower_limit[i]]
            )
            % MOD
        )
        continue
    n_over_d_as_gcd_sum.append(
        (
            (n_over_d_possible_values[i] - n_over_d_possible_values[i - 1])
            * (n_over_d_possible_values[i] + n_over_d_possible_values[i - 1] + 1)
            // 2
            * i_square_phi_i_acc_sum[n_over_d_lower_limit[i]]
        )
        % MOD
    )
print(sum(n_over_d_as_gcd_sum) % MOD)