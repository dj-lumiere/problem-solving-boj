# 29616 인기투표

from fractions import Fraction
from math import lcm, ceil
from sys import stdin


def input():
    return stdin.readline().strip()


N, P = map(int, input().split(" "))

last_percentage = list(map(int, input().split(" ")))
last_percentage = [Fraction(i, 10 ** (P + 2)) for i in last_percentage]
least_voter_at_last = lcm(*[i.denominator for i in last_percentage])
last_voter = [int(i * least_voter_at_last) for i in last_percentage]

current_percentage = list(map(int, input().split(" ")))
current_percentage = [Fraction(i, 10 ** (P + 2)) for i in current_percentage]
least_voter_at_current = lcm(*[i.denominator for i in current_percentage])
current_voter = [int(i * least_voter_at_current) for i in current_percentage]

minimum_multiplier_to_match = max(
    [ceil(Fraction(v1, v2)) if v2 else 1 for v1, v2 in zip(last_voter, current_voter)]
)

current_voter = [i * minimum_multiplier_to_match for i in current_voter]
least_voter_at_current *= minimum_multiplier_to_match

print(least_voter_at_last, least_voter_at_current)