# 16722 결! 합!

from itertools import combinations
from sys import stdin


def input():
    return stdin.readline().strip()


def is_hap(card_set, N):
    properties = [[0] * N for _ in range(N)]
    for t in card_set:
        for i in range(N):
            x = t[i]
            properties[i][x] += 1
    for property_sub in properties:
        if any(i == N for i in property_sub) or all(i == 1 for i in property_sub):
            continue
        return False
    return True


card = []
symbol = {"CIRCLE": 0, "TRIANGLE": 1, "SQUARE": 2}
color = {"YELLOW": 0, "RED": 1, "BLUE": 2}
background = {"GRAY": 0, "WHITE": 1, "BLACK": 2}
hap = []
for _ in range(9):
    s, c, b = input().split(" ")
    card.append((symbol[s], color[c], background[b]))
for card_set in combinations(range(1, 9 + 1), 3):
    if is_hap(map(lambda x: card[x - 1], card_set), 3):
        hap.append(list(card_set))
score = 0
N = int(input())
hap_visited = [False] * len(hap)
gyul_visited = False
for _ in range(N):
    op, *numbers = input().split(" ")
    numbers = list(map(int, numbers))
    numbers.sort()
    if op == "H" and hap and numbers in hap and not hap_visited[hap.index(numbers)]:
        hap_visited[hap.index(numbers)] = True
        score += 1
        continue
    if op == "G" and (not hap or all(hap_visited)) and not gyul_visited:
        gyul_visited = True
        score += 3
        continue
    score -= 1
print(score)