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
        numbers = [int(input())]
        while True:
            next_number = numbers[-1]
            if next_number == 1:
                break
            if next_number % 2 == 1:
                next_number += 1
            else:
                next_number //= 2
            numbers.append(next_number)
        answer = len(numbers) - 1
        answers[h] = f"{answer}"
    print(answers)