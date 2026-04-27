import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        l = int(input())
        t = [int(input()) for _ in range(n)]
        t.sort()
        tape_cluster = [1 for _ in range(n)]
        current_position = t[0]
        for i, v in enumerate(t):
            if i == 0:
                continue
            if abs(v - current_position) > l - 1:
                tape_cluster[i] = tape_cluster[i - 1] + 1
                current_position = v
            else:
                tape_cluster[i] = tape_cluster[i - 1]
        answer = tape_cluster[-1]
        answers[h] = (f"{answer}")
    print(answers)