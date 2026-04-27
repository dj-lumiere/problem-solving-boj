answers = []
for i in range(1, 10**18):
    n, *numbers = map(int, input().split())
    if n == 0:
        break
    answer = numbers[n//2] if n % 2 == 1 else (numbers[n//2-1]+numbers[n//2])/2
    answers.append(f"Case {i}: {answer:.1f}")
print(*answers, sep="\n")