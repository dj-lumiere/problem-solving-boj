# 14698 전생했더니 슬라임 연구자였던 건에 대하여 (Hard)

from heapq import heapify, heappop, heappush
from sys import stdin

MOD = 1_000_000_007


def input():
    return stdin.readline().strip()


def find_minimal_slime_form_energy(slime_sizes: list[int]) -> int:
    heapify(slime_sizes)
    result = 1
    if len(slime_sizes) == 1:
        return 1
    while len(slime_sizes) > 1:
        target1 = heappop(slime_sizes)
        target2 = heappop(slime_sizes)
        result *= target1 * target2
        heappush(slime_sizes, target1 * target2)
    return result % MOD


T = int(input())
for _ in range(T):
    _ = int(input())
    slime_sizes = list(map(int, input().split(" ")))
    print(find_minimal_slime_form_energy(slime_sizes))
