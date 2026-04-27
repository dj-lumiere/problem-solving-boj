import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        a = input().decode().strip()
        b = input().decode().strip()
        answer = []
        for k in range(len(a)):
            answer_sub = 0
            recent_found = 0
            #eprint(a[k:])
            target = a[k:]
            for i, v in enumerate(target, start=1):
                #eprint((i, recent_found, i - len(b), target[i - len(b):i]))
                if i < len(b):
                    continue
                if i - recent_found < len(b):
                    continue
                if target[i - len(b):i] == b:
                    answer_sub += 1
                    recent_found = i
            #eprint(answer_sub)
            answer.append(answer_sub)
        answers[h] = f"{max(answer)}"
    print(answers)