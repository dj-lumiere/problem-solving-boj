import os
from collections import deque

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        student_queue = deque()
        food_queue = deque()
        a = []
        b = []
        c = []
        n = int(input())
        for _ in range(n):
            opcode = int(input())
            if opcode == 1:
                student_queue.append((int(input()), int(input())))
            if opcode == 2:
                x, y = student_queue.popleft()
                food = int(input())
                if y == food:
                    a.append(x)
                else:
                    b.append(x)
        if student_queue:
            while student_queue:
                x, y = student_queue.popleft()
                c.append(x)
        a.sort()
        b.sort()
        c.sort()
        answer = [(" ".join(map(str, a)) if a else "None"), (" ".join(map(str, b)) if b else "None"),
                  (" ".join(map(str, c)) if c else "None")]
        answers[i] = "\n".join(answer)
    print(answers)