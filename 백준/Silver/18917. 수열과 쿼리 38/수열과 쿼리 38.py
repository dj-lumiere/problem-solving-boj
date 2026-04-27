import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    sums = 0
    xors = 0
    print_queries = 0
    for h in range(t):
        opcode = int(input())
        if opcode == 1:
            operand = int(input())
            sums += operand
            xors ^= operand
        if opcode == 2:
            operand = int(input())
            sums -= operand
            xors ^= operand
        if opcode == 3:
            answers[print_queries] = f"{sums}"
            print_queries += 1
        if opcode == 4:
            answers[print_queries] = f"{xors}"
            print_queries += 1
    print(answers[:print_queries])