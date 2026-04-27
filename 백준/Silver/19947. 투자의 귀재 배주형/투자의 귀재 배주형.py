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
        h = int(input())
        y = int(input())
        answer = [h for _ in range(y+1)]
        for j, v in enumerate(answer):
            if j == 0:
                continue
            candidates = []
            if j >= 1:
                candidates.append(answer[j-1] * 105 // 100)
            if j >= 3:
                candidates.append(answer[j-3] * 120 // 100)
            if j >= 5:
                candidates.append(answer[j-5] * 135 // 100)
            answer[j] = max(candidates)
        answers[i] = f"{answer[y]}"
    print(answers)
