import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for h in range(t):
        pass
    while True:
        n = int(input())
        if n == 0:
            break
        answer = []
        start = 0
        end = 51
        while start + 1 < end:
            mid = (start + end) // 2
            answer.append(mid)
            if mid > n:
                end = mid
            elif mid < n:
                start = mid
            else:
                break
        answers.append(" ".join(map(str, answer)))
    print(answers)