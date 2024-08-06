answers = []
INF = 10 ** 18
t = 10
for hh in range(t):
    n, m = input().split()
    n = int(n)
    password = list(map(int, m))
    stack = []
    for i, v in enumerate(password):
        if not stack:
            stack.append(v)
            continue
        if stack[-1] == v:
            stack.pop()
            continue
        stack.append(v)
    answer = "".join(map(str, stack))
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")
