import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        balls = [int(input()) for _ in range(n)]
        base = [False for _ in range(3)]
        consecutive_balls = 0
        score = 0
        for i, v in enumerate(balls):
            if v == 1 and consecutive_balls <= 3:
                consecutive_balls += 1
            elif v == 3 and consecutive_balls <= 3:
                consecutive_balls += 1
                if base.pop():
                    score += 1
                base.insert(0, False)
            if v == 2 or consecutive_balls == 4:
                new_base = [False for _ in range(4)]
                new_base[0] = True
                if base[0]:
                    new_base[1] = True
                else:
                    new_base[1] = base[1]
                if base[0] and base[1]:
                    new_base[2] = True
                else:
                    new_base[2] = base[2]
                if base[0] and base[1] and base[2]:
                    new_base[3] = True
                score += 1 if new_base.pop() else 0
                base = new_base
                consecutive_balls = 0
        answer = score
        answers[h] = f"{score}"
    print(answers)