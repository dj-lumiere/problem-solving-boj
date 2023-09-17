N = int(input())
solved_problem = list(map(int, input().split(" ")))
streak = []
for problem_count in solved_problem:
    if not problem_count and (not streak or streak[-1] != 0):
        streak.append(0)
        continue
    if not problem_count:
        continue
    if problem_count and not streak:
        streak.append(1)
        continue
    if problem_count and streak:
        streak[-1] += 1
        continue
print(max(streak))