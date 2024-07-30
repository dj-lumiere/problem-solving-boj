answers = []
t = int(input())
for hh in range(t):
    a, b, c = map(int, input().split())
    candidates = [a - (2 * b - c), b - (a + c) / 2, c - (2 * b - a)]
    candidates.extend([-i for i in candidates])
    candidates = [i for i in candidates if i >= 0]
    answer = f"#{hh + 1} {min(candidates):.1f}"
    answers.append(f"{answer}")
print(*answers, sep="\n")