# A번 - Knob

from sys import stdin


def input():
    return stdin.readline().strip()


T = int(input())
knob_list = [tuple(map(int, input().split(" "))) for _ in range(T)]
fun_factor = 0
for i, (l, r) in enumerate(knob_list):
    if l == r and not (l == r == 0):
        fun_factor += 1
    if i == 0:
        continue
    l_prev, r_prev = knob_list[i - 1]
    if l_prev == l and not (l_prev == l == 0):
        fun_factor += 1
    if r_prev == r and not (r_prev == r == 0):
        fun_factor += 1
print(fun_factor)