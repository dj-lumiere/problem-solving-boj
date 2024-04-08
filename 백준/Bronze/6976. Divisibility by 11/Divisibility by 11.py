import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        next_n = n
        numbers = [next_n]
        while next_n >= 99:
            next_n, delete = divmod(next_n, 10)
            next_n -= delete
            if next_n <= 0:
                continue
            numbers.append(next_n)
        if numbers[-1] % 11 == 0:
            answers[i] = "\n".join(map(str, numbers)) + f"\nThe number {n} is divisible by 11."
        else:
            answers[i] = "\n".join(map(str, numbers)) + f"\nThe number {n} is not divisible by 11."
    print(answers)