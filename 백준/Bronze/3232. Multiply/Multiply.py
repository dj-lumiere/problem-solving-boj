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
        p, q, r = [int(input()) for _ in range(3)]
        answer = 0
        minimal_base = max(2, max(list(map(int, str(p))) + list(map(int, str(q))) + list((map(int, str(r))))) + 1)
        for j in range(minimal_base, 17):
            p2 = int(str(p), base=j)
            q2 = int(str(q), base=j)
            r2 = int(str(r), base=j)
            if p2 * q2 == r2:
                answer = j
                break
        answers[i] = f"{answer}"
    print(answers)