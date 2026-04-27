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
        n = int(input())
        m = int(input())
        lamp = [[] for _ in range(n)]
        for i in range(n):
            a = int(input())
            for _ in range(a):
                lamp[i].append(int(input()))
        for i in range(n):
            turned_on = [True] + [False for _ in range(m)]
            for j in range(n):
                if j == i:
                    continue
                for k in lamp[j]:
                    turned_on[k] = True
            if all(turned_on):
                answers[h] = "1"
                break
        else:
            answers[h] = "0"
    print(answers)