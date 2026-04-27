import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        positions = [int(input()) for _ in range(4)]
        sx, sy, ex, ey = positions
        results = []
        for i in range(n):
            m = int(input())
            cur_x, cur_y = sx, sy
            current_distance = 0
            for j in range(m):
                x, y = int(input()), int(input())
                current_distance += abs(x - cur_x) + abs(y - cur_y)
                cur_x, cur_y = x, y
            current_distance += abs(ex - cur_x) + abs(ey - cur_y)
            results.append(current_distance)
        answer = results.index(min(results)) + 1
        answers[h] = f"{answer}"
    print(answers)