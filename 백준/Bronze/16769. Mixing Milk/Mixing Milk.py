import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    INF = 10 ** 18
    for h in range(t):
        a_cap, a = int(input()), int(input())
        b_cap, b = int(input()), int(input())
        c_cap, c = int(input()), int(input())
        for i in range(100):
            if i % 3 == 0:
                b += a
                a = 0
                if b > b_cap:
                    a += b - b_cap
                    b = b_cap
            if i % 3 == 1:
                c += b
                b = 0
                if c > c_cap:
                    b += c - c_cap
                    c = c_cap
            if i % 3 == 1:
                a += c
                c = 0
                if a > a_cap:
                    c += a - a_cap
                    a = a_cap
        answers[h] = (f"{a}\n{b}\n{c}")
    print(answers)