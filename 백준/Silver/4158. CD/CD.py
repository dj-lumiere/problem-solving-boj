from os import write

print = lambda x: write(1, "\n".join(x).encode())
t = 0
answers = ["" for _ in range(0)]
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    a = set([int(input()) for _ in range(n)])
    b = set([int(input()) for _ in range(m)])
    answer = len(a.intersection(b))
    answers.append(f"{answer}")
print(answers)