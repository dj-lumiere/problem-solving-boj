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
        first = input().decode()
        has_been_worshipped = set()
        n = int(input())
        for _ in range(n):
            win, lose = input().decode(), input().decode()
            if first == lose:
                has_been_worshipped.add(first)
                first = win
        has_been_worshipped.add(first)
        answers[i] = f"{first}\n{len(has_been_worshipped)}"
    print(answers)