import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    for h in range(t):
        pass
    while True:
        n = int(input())
        if n == 0:
            break
        t += 1
        answer = 0
        while n > 0:
            answer += n // 5
            n //= 5
        answers.append(f"Case #{t}: {answer}")
    print(answers)