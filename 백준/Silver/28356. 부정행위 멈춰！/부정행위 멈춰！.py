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
        k = 4
        if n == m == 1:
            k = 1
        elif n == 1 or m == 1:
            k = 2
        answer = [[0 for _ in range(m)] for _ in range(n)]
        if k == 1:
            answer[0][0] = 1
        elif k == 2 and n == 1:
            for i in range(m):
                answer[0][i] = 2 if i % 2 == 1 else 1
        elif k == 2 and m == 1:
            for i in range(n):
                answer[i][0] = 2 if i % 2 == 1 else 1
        else:
            for i in range(n):
                for j in range(m):
                    answer[i][j] = (i % 2) * 2 + (j % 2) + 1
        answers[h] = f"{k}\n" + "\n".join(" ".join(map(str, x)) for x in answer)
    print(answers)