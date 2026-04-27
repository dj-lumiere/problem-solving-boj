import os
from bisect import bisect_left

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        N_str, *operations = map(lambda x: x.decode(), input().split())
        N = int(float(N_str) * 10)
        for v in operations:
            if v == "@":
                N *= 3
            if v == "%":
                N += 50
            if v == "#":
                N -= 70
        answers[i] = f"{N / 10:.2f}"
    # while True:
    #     n = int(input())
    #     if n == 0:
    #         break
    #     a = [int(input()) for _ in range(n)]
    #     answers.append("\n".join(map(str, reversed(a)))+"\n0")
    print(answers)