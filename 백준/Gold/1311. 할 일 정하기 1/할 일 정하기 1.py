# 1311 할 일 정하기 1

from sys import stdin


def input():
    return stdin.readline().strip()


def assign_work(current_person, visited):
    if current_person >= N and visited == COMPLETE:
        return 0
    if current_person >= N and visited != COMPLETE:
        return INF
    result = workflow_price[current_person][visited]
    if result != -1:
        return result
    result = INF
    for next_task in range(N):
        if visited & (1 << next_task):
            continue
        result = min(
            result,
            assign_work(current_person + 1, visited | (1 << next_task))
            + work_price[current_person][next_task],
        )
    workflow_price[current_person][visited] = result
    return result


N = int(input())
work_price = [list(map(int, input().split(" "))) for _ in range(N)]
INF = 10000 * N + 1
workflow_price = [[-1 for _ in range(1 << N)] for _ in range(N)]
COMPLETE = (1 << N) - 1
result = assign_work(0, 0)
print(result)