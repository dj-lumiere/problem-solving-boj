import os

tokens = iter(map(int, os.read(0, os.fstat(0).st_size).split()))
t = next(tokens)
answers = ["" for _ in range(t)]
for i in range(t):
    n = next(tokens)
    candy_count = [next(tokens) for _ in range(n)]
    if sum(candy_count) % n:
        answers[i] = "NO"
    else:
        answers[i] = "YES"
print(*answers, sep="\n")