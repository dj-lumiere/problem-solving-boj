t = int(input())
answers = []
for hh in range(1, t + 1):
    n, a, b = map(int, input().split())
    answer1 = min(b * (n - i * i) for i in range(1, int(n ** .5) + 1))
    answer2 = min(a * abs((n // i - i)) + b * (n - i * (n // i)) for i in range(1, int(n ** .5) + 1))
    answer = min(answer1, answer2)
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")
