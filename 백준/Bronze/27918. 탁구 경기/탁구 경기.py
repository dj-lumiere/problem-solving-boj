# 27918 탁구 경기

from sys import stdin

N: int = int(stdin.readline().strip())
dalgu_score: int = 0
ponix_score: int = 0
for _ in range(N):
    person_scored: str = stdin.readline().strip()
    if person_scored == "D":
        dalgu_score += 1
    else:
        ponix_score += 1
    if abs(dalgu_score - ponix_score) >= 2:
        break
print(f"{dalgu_score}:{ponix_score}")