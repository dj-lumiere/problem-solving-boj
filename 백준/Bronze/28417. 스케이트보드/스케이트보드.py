# 28417 스케이트보드

from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def get_score(score_list: list[int]) -> int:
    return max(score_list[:2]) + sum(sorted(score_list[2:], reverse=True)[:2])


N = int(input())
scores = []
for _ in range(N):
    score_list = list(map(int, input().split(" ")))
    scores.append(get_score(score_list))
print(f"{max(scores)}")