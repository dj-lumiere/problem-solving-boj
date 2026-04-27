import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        divisors = []
        for j in range(1, int(n ** .5) + 1):
            if n % j == 0:
                divisors.extend([j, n // j])
        divisors = list(set(divisors))
        is_over_number = sum(divisors) - n > n
        is_divisor_not_over = True
        for v in divisors:
            if v == n:
                continue
            divisors = []
            for j in range(1, int(v ** .5) + 1):
                if v % j == 0:
                    divisors.extend([j, v // j])
            divisors = list(set(divisors))
            if sum(divisors) - v > v:
                is_divisor_not_over = False
                break
        answers[i] = "Good Bye" if is_over_number and is_divisor_not_over else "BOJ 2022"
    print(answers)