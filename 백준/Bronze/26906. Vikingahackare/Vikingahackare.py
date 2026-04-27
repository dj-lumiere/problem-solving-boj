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
        change_table = {}
        n = int(input())
        for _ in range(n):
            char, binary = input().decode(), input().decode()
            change_table[binary] = char
        number_sequence = input().decode()
        current_sequence = ""
        answer = ""
        for j, v in enumerate(number_sequence, start=1):
            current_sequence += v
            if j % 4 == 0:
                answer += change_table[current_sequence] if current_sequence in change_table else "?"
                current_sequence = ""
        answers[i] = answer
    print(answers)