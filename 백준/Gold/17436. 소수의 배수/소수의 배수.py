from os import write

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        n = int(input())
        m = int(input())
        primes = [int(input()) for _ in range(n)]
        answer = m
        for mask in range(1, 1<<n):
            contain = [mask & (1<<i) != 0 for i in range(n)]
            modify_sign = 1
            divisor = 1
            if sum(contain) % 2 == 1:
                modify_sign = -1
            for i, v in enumerate(contain):
                if v:
                    divisor *= primes[i]
            answer += modify_sign * (m // divisor)
        answer = m - answer
        answers.append(f"{answer}")
    print(*answers,end="\n")