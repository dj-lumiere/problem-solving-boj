answers = []
t = int(input())
for hh in range(t):
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    q = int(input())
    result = []
    for _ in range(q):
        y = int(input()) - 1
        result.append(s[y % n] + t[y % m])
    answer = f"#{hh + 1} " + " ".join(result)
    answers.append(f"{answer}")
print(*answers, sep="\n")