# 30035 Tier and Rank

from math import ceil
from sys import stdin


def input():
    return stdin.readline().strip()


N, T = map(int, input().split(" "))
current_rank = 1
tier_rank = {}
for _ in range(T):
    tier, person = input().split(" ")
    if person.endswith("%"):
        tier_person = N * int(person[:-1]) // 100
    else:
        tier_person = min(N, int(person))
    subtier_person = ceil(tier_person / 4)
    current_subtier_rank = current_rank
    tier_rank[f"{tier}"] = (current_rank, current_rank + tier_person - 1)
    for i in range(1, 4 + 1):
        tier_rank[f"{tier}{i}"] = (
            current_subtier_rank,
            min(current_subtier_rank + subtier_person, current_rank + tier_person) - 1,
        )
        current_subtier_rank += subtier_person
    current_rank += tier_person
    N -= tier_person
target_rank = input()
possible_rank_min, possible_rank_max = tier_rank[target_rank]
if N:
    print("Invalid System")
elif possible_rank_max - possible_rank_min < 0:
    print("Liar")
else:
    print(possible_rank_min, possible_rank_max)