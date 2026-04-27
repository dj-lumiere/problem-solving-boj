import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    # t = 1
    # answers = ["" for _ in range(t)]
    # for i in range(t):
    answers = []
    while True:
        n = input().decode()
        if n == "0":
            break
        possible_random_numbers = {n}
        current_number = int(n)
        while True:
            next_number = f"{current_number ** 2:0>8}"[2:6]
            if next_number in possible_random_numbers:
                break
            possible_random_numbers.add(next_number)
            current_number = int(next_number)
        answers.append(str(len(possible_random_numbers)))
    print(answers)