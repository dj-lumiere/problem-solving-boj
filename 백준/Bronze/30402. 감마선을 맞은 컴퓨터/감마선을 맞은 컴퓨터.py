# 30402 감마선을 맞은 컴퓨터
from collections import Counter

color_grid = []
for _ in range(15):
    color_grid.extend(list(input().split(" ")))
color_count = Counter(color_grid)
if "w" in color_count:
    print("chunbae")
elif "b" in color_count:
    print("nabi")
else:
    print("yeongcheol")