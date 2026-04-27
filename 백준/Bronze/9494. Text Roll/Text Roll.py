import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    for i in range(t):
        pass
    while True:
        n = int(input())
        if n == 0:
            break
        lines = [input().decode().split() for _ in range(n)]
        current_cursor = 0
        for line in lines:
            current_word = 0
            for word in line:
                current_word += len(word)
                if current_word >= current_cursor:
                    current_cursor = current_word
                    break
                current_word += 1
        answers.append(f"{current_cursor + 1}")
    print(answers)