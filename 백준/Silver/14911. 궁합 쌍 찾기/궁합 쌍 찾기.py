import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        numbers = list(map(int, input().decode().split()))
        m = int(input())
        pairs = set()
        for i1, v1 in enumerate(numbers):
            for i2, v2 in enumerate(numbers):
                if i1 == i2:
                    continue
                if v1 + v2 == m:
                    pairs.add((min(v1, v2), max(v1, v2)))
        answer = "\n".join(f"{x[0]} {x[1]}" for x in sorted(pairs)) + f"\n{len(pairs)}" if pairs else "0"
        answers[h] = f"{answer}"
    print(answers)