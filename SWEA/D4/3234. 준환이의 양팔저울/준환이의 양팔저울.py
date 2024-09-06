from itertools import permutations

t = int(input())
answers = []
for hh in range(1, t + 1):
    n = int(input())
    a = list(map(int, input().split()))
    answer = 0
    stack = [(0, 0)]
    for b in permutations(a):
        # start, left-right
        while stack:
            start, current_weight_difference = stack.pop()
            # eprint((start, end, count, current_weight_difference, path))
            if start == n:
                answer += 1
                continue
            stack.append((start + 1, current_weight_difference + b[start]))
            if current_weight_difference - b[start] >= 0:
                stack.append((start + 1, current_weight_difference - b[start]))
        stack.clear()
        stack.append((0, 0))
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")
