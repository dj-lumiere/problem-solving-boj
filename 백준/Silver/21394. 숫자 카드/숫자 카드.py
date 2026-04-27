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
        numbers = [int(input()) for _ in range(9)]
        cards = []
        for j, v in enumerate(numbers, start=1):
            if j == 6:
                cards.extend([9] * v)
            else:
                cards.extend([j] * v)
        cards.sort(reverse=True)
        answer = [0 for _ in range(len(cards))]
        for j, v in enumerate(cards):
            if j % 2 == 1:
                answer[-j // 2] = v
            else:
                answer[j // 2] = v
        answers[i] = " ".join(map(str, answer))
    print(answers)