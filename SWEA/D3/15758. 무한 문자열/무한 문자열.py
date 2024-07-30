answers = []
t = int(input())
for hh in range(t):
    a, b = input().split()
    a *= len(b)
    b *= len(a)//len(b)
    answer = f"#{hh + 1} {'yes' if a==b else 'no'}"
    answers.append(f"{answer}")
print(*answers, sep="\n")