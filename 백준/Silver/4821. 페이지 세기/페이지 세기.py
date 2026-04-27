import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
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
        page = [False for _ in range(n + 1)]
        page_range = input().decode().split(",")
        for j in page_range:
            if "-" in j:
                s, e = map(int, j.split("-"))
                if s > e:
                    continue
                if e >= n:
                    e = n
                if s > n:
                    continue
                page[s:e + 1] = [True] * (e - s + 1)
            else:
                s = int(j)
                if s>n:
                    continue
                page[s] = True
        answers.append(f"{sum(page)}")
    print(answers)