import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    table = {
        ("A", "A"): "A",
        ("A", "G"): "C",
        ("A", "C"): "A",
        ("A", "T"): "G",
        ("G", "A"): "C",
        ("G", "G"): "G",
        ("G", "C"): "T",
        ("G", "T"): "A",
        ("C", "A"): "A",
        ("C", "G"): "T",
        ("C", "C"): "C",
        ("C", "T"): "G",
        ("T", "A"): "G",
        ("T", "G"): "A",
        ("T", "C"): "G",
        ("T", "T"): "T",
    }
    for i in range(t):
        n = int(input())
        code = list(input().decode())
        while len(code) > 1:
            a_n_1, a_n = code[-2:]
            code.pop()
            code.pop()
            code.append(table[(a_n_1, a_n)])
        answers[i] = code[0]
    print(answers)