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
        k = int(input())
        m = int(input())
        numbers = [int(input()) for _ in range(n)]
        for i in range(m):
            opcode = int(input())
            flip_target = (1, opcode) if opcode > 0 else (n+opcode+1,n)
            if not flip_target[0]<=k<=flip_target[1]:
                continue
            k = flip_target[0]+(flip_target[1]-k)
        answer = k
        answers[h] = f"{answer}"
    print(answers)