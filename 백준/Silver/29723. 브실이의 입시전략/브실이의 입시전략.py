# S번 - 브실이의 입시전략
from sys import stdin


def input():
    return stdin.readline().strip()


N, M, K = map(int, input().split(" "))
score = {i[0]: int(i[1]) for i in [input().split(" ") for _ in range(N)]}
special_subject = list([input() for _ in range(K)])
answer_max, answer_min = 0, 0
for i in special_subject:
    answer_max += score[i]
    answer_min += score[i]
    score.pop(i)
non_special_subject = list(score.values())
non_special_subject.sort()
answer_min += sum(non_special_subject[: M - K]) if M - K else 0
answer_max += sum(non_special_subject[-(M - K) :]) if M - K else 0
print(answer_min, answer_max)