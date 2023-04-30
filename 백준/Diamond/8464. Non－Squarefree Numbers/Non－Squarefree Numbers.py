# 8464 Non-Squarefree Numbers

from math import sqrt


def sieve_mobius(n):
    # actual mobius value list
    mobius_list = [1 for _ in range(n + 1)]
    # prime checking list
    is_prime = [True for _ in range(n + 1)]
    # µ(1) = 1
    mobius_list[1] = 1
    for i in range(2, n + 1):
        if is_prime[i]:
            # has at least one prime factor.
            mobius_list[i] = -1
            for j in range(i*2, n+1, i):
                # has at least two prime factors
                is_prime[j] = False
                # has at least one prime squared factors
                if j % (i*i) == 0:
                    mobius_list[j] = 0
                else:
                    mobius_list[j] *= -1
    return mobius_list

# Count of square-free numbers in [1, x] = Σ (x // (i * i) * µ(i))
def find_kth_non_square_free_number(k, mobius):
    left = 1
    right = k * 4
    while left < right:
        mid = (left + right) // 2
        count = mid
        for i in range(1, int(mid**0.5) + 1):
            count -= mobius[i] * (mid // (i * i))
        if count < k:
            left = mid + 1
        else:
            right = mid
    return left


# Precompute the Möbius function values using the Sieve of Eratosthenes
n = int((4*10**10)**.5) + 1
mobius_list = sieve_mobius(n)

# Read the input
k = int(input())

# Find the k-th square-free number
kth_non_square_free_number = find_kth_non_square_free_number(k, mobius_list)

# Print the result
print(kth_non_square_free_number)
