# 29730 임스의 데일리 인증 스터디

from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
study: list[str] = []
problems = []
for _ in range(N):
    study_sub = input()
    if study_sub.startswith("boj.kr/"):
        problems.append(int(study_sub[7:]))
    else:
        study.append(study_sub)
study.sort(key=lambda x: (len(x), x))
problems.sort()
if study:
    print(*study, sep="\n")
print(*[f"boj.kr/{i}" for i in problems], sep="\n")