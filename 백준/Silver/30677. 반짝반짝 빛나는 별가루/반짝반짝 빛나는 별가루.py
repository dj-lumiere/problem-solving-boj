# Orange번 - 반짝반짝 빛나는 별가루
from sys import stdin


def input():
    return stdin.readline().strip()


def delta_stardust(
    base_stardust_count, combo, combo_coefficient, skill, skill_coefficient
):
    return (
        (base_stardust_count * (100 + combo * combo_coefficient))
        * (100 + skill * skill_coefficient)
        // 10000
    )


N, K, C, R = map(int, input().split(" "))
base = [0] + list(map(int, input().split(" ")))
s = [0] + list(map(int, input().split(" ")))
p = [0] + list(map(int, input().split(" ")))
l = [int(input()) for _ in range(N)]
magic_count = [0] * (K + 1)
stardust = 0
fatigue = 0
combo = 0
for magic_number in l:
    if magic_number == 0:
        fatigue = max(fatigue - R, 0)
        combo = 0
        continue
    stardust += delta_stardust(
        base[magic_number], combo, C, magic_count[magic_number], s[magic_number]
    )
    fatigue += p[magic_number]
    combo += 1
    magic_count[magic_number] += 1
    if fatigue > 100:
        stardust = -1
        combo = 0
        fatigue = 0
        break
print(stardust)