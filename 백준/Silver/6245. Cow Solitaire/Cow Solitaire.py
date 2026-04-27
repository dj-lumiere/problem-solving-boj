import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    card_number = {"A": 1, "K": 13, "Q": 12, "J": 11, "T": 10}
    for i in range(2, 10):
        card_number[str(i)] = i
    for a in range(t):
        n = int(input())
        card_grid = [[card_number[input().decode()[0]] for _ in range(n)] for _ in range(n)]
        answer = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):  # column
            for j in range(n):  # row
                if i == n - 1 and j == 0:
                    answer[j][i] = card_grid[j][i]
                elif i == n-1:
                    answer[j][i] = answer[j-1][i] + card_grid[j][i]
                elif j == 0:
                    answer[j][i] = answer[j][i+1] + card_grid[j][i]
                else:
                    answer[j][i] = max(answer[j][i + 1] + card_grid[j][i], answer[j-1][i] + card_grid[j][i])
        answers[a] = f"{answer[-1][0]}"
    print(answers)