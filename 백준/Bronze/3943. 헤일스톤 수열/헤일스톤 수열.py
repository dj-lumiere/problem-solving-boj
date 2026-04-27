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
        n = int(input())
        seq = [n]
        while True:
            last = seq[-1]
            if last == 1:
                break
            if last % 2 == 1:
                seq.append(last*3+1)
            else:
                seq.append(last//2)
        answers[i] = f"{max(seq)}"
    print(answers)