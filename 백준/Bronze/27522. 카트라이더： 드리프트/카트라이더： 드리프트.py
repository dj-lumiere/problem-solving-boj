# 27522 카트라이더: 드리프트

racer_time_list: list[tuple] = []
for _ in range(8):
    time, team = list(map(str, input().split(" ")))
    time_min, time_sec, time_ms = list(map(int, time.split(":")))
    racer_time_list.append(((time_min * 60 + time_sec) * 1000 + time_ms, team))
racer_time_list = sorted(racer_time_list, key=lambda x:x[0])
rank_score: list[int] = [10, 8, 6, 5, 4, 3, 2, 1]
red_score: int = 0
blue_score: int = 0
for i, (j, k) in enumerate(racer_time_list):
    if k == "R":
        red_score += rank_score[i]
    else:
        blue_score += rank_score[i]
print("Red" if red_score > blue_score else "Blue")