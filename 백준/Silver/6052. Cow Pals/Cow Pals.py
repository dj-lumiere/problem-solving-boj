import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        answer = ""
        for i in range(n, 100001):
            divisors = set()
            for j in range(1, int(i ** .5) + 1):
                if i % j == 0:
                    divisors.add(j)
                    divisors.add(i // j)
            pal = sum(divisors) - i
            pal_divisors = set()
            for j in range(1, int(pal ** .5) + 1):
                if pal % j == 0:
                    pal_divisors.add(j)
                    pal_divisors.add(pal // j)
            if sum(pal_divisors) - pal == i and i != pal:
                answer = f"{i} {pal}"
                break
        answers[h] = f"{answer}"
    print(answers)