# 29155 개발자 지망생 구름이의 취업 뽀개기

from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
question_count = [0] + list(map(int, input().split(" ")))
question_required_time = [[] for _ in range(6)]
for _ in range(N):
    difficulty, required_time = map(int, input().split(" "))
    question_required_time[difficulty].append(required_time)
for i in range(1, 5 + 1):
    question_required_time[i].sort()
result = 0
for i in range(1, 5 + 1):
    solve_problem_count = question_count[i]
    solve_problem = question_required_time[i][:solve_problem_count]
    result += (
        sum(solve_problem)
        + sum([v2 - v1 for v2, v1 in zip(solve_problem[1:], solve_problem)])
        + 60
    )
result -= 60
print(result)