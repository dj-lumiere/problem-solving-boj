# 20529 가장 가까운 세 사람의 심리적 거리

from collections import Counter
from itertools import combinations


def mental_distance(personality_type1: str, personality_type2: str) -> int:
    return sum([a != b for a, b in zip(personality_type1, personality_type2)])


def three_people_mental_difference(
    personality_type1: str, personality_type2: str, personality_type3: str
) -> int:
    return (
        mental_distance(personality_type1, personality_type2)
        + mental_distance(personality_type2, personality_type3)
        + mental_distance(personality_type3, personality_type1)
    )


def minimal_mental_difference(personalities: list[str]) -> int:
    personalities_count = Counter(personalities)
    minimal_distance = 13
    for personality_type1, quantity in personalities_count.items():
        if quantity >= 3:
            return 0
    for personality_type1, personality_type2 in combinations(
        personalities_count.keys(), 2
    ):
        if personalities_count[personality_type1] >= 2:
            minimal_distance = min(
                minimal_distance,
                three_people_mental_difference(
                    personality_type1, personality_type1, personality_type2
                ),
            )
        if personalities_count[personality_type2] >= 2:
            minimal_distance = min(
                minimal_distance,
                three_people_mental_difference(
                    personality_type1, personality_type2, personality_type2
                ),
            )
    for personality_type1, personality_type2, personality_type3 in combinations(
        personalities_count.keys(), 3
    ):
        minimal_distance = min(
            minimal_distance,
            three_people_mental_difference(
                personality_type1, personality_type2, personality_type3
            ),
        )
    return minimal_distance


T = int(input())
for _ in range(T):
    n = int(input())
    personalities = input().split(" ")
    print(minimal_mental_difference(personalities))