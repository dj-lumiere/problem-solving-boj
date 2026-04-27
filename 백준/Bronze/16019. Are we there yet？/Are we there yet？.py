import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        numbers = [int(input()) for _ in range(4)]
        acc_sum = [0]
        answer = []
        for num in numbers:
            acc_sum.append(acc_sum[-1]+num)
        for j, v in enumerate(acc_sum):
            answer.append([abs(k-v) for k in acc_sum])
        answers[i] = "\n".join(" ".join(map(str, j)) for j in answer)
    print(answers)