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
        a, b = int(input()), int(input())
        r = int(input())
        flowers = [[0 for _ in range(r - i)] for i in range(r)]
        time = 1
        current_pos = (a, b)
        while True:
            current_a, current_b = current_pos[0], current_pos[1]
            flowers[current_a][current_b] += 1
            next_pos = (current_a + 1, current_b + 1) if current_a + current_b + 2 < r else (
            current_a // 2, current_b // 2)
            if flowers[next_pos[0]][next_pos[1]] > 0:
                break
            time += 1
            current_pos = next_pos
        answer = time
        answers[h] = f"{answer}"
    print(answers)