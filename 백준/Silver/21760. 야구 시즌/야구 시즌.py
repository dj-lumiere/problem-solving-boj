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
        n, m, k, d = [int(input()) for _ in range(4)]
        # total_match = n*mC2*A+nC2*m*m*B=mC2*k*B+nC2*m*m*B
        coefficient = (n * m * (m - 1) * k + n * (n - 1) * m * m) // 2
        b = d // coefficient
        if b == 0:
            answers[i] = "-1"
        else:
            answers[i] = f"{b * coefficient}"
    print(answers)