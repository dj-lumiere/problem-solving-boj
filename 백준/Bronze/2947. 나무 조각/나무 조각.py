import os
import re

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    t = 1
    answers = []
    for i in range(t):
        numbers = [int(next(tokens)) for i in range(5)]
        while numbers != [1,2,3,4,5]:
            if numbers[0] > numbers[1]:
                numbers[0], numbers[1] = numbers[1], numbers[0]
                answers.append(f'{" ".join(map(str, numbers))}')
            if numbers[1] > numbers[2]:
                numbers[1], numbers[2] = numbers[2], numbers[1]
                answers.append(f'{" ".join(map(str, numbers))}')
            if numbers[2] > numbers[3]:
                numbers[2], numbers[3] = numbers[3], numbers[2]
                answers.append(f'{" ".join(map(str, numbers))}')
            if numbers[3] > numbers[4]:
                numbers[3], numbers[4] = numbers[4], numbers[3]
                answers.append(f'{" ".join(map(str, numbers))}')
    print(answers)