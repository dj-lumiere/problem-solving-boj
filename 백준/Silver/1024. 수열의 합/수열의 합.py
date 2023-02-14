# 1024 수열의 합

N, L = list(map(int, input().split(" ")))

answer_length = 101
answer_start = 0


def to_N_sum(N: int):
    if N % 2:
        return (N + 1) // 2 * N
    else:
        return N // 2 * (N + 1)


for i in range(L, 100 + 1):
    quot, mod = divmod(N - to_N_sum(i), i)
    if not mod and i < answer_length:
        answer_length = i
        answer_start = quot
if answer_length > 100 or answer_start < -1:
    print(-1)
else:
    print(" ".join(map(str, [answer_start + i for i in range(1, answer_length + 1)])))