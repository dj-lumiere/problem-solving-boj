# 4357 이산 로그

from typing import Optional
from math import floor
from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def discrete_logarithm(P: int, B: int, N: int) -> Optional[int]:
    m = floor(P ** 0.5)
    baby_step_dict = dict()
    giant_step_dict = dict()
    baby_step = N
    giant_step = 1
    B_m = pow(B, m, P)
    modular_inverse = pow(B, -1, P)
    for i in range(0, m + 1):
        if baby_step not in baby_step_dict:
            baby_step_dict[baby_step] = i
        if giant_step not in giant_step_dict:
            giant_step_dict[giant_step] = i
        baby_step = baby_step * modular_inverse % P
        giant_step = giant_step * B_m % P

    any_matches = []
    for baby_step, baby_index in baby_step_dict.items():
        if baby_step in giant_step_dict:
            giant_index = giant_step_dict[baby_step]
            x_candidate = baby_index + giant_index * m
            any_matches.append(x_candidate)

    if any_matches:
        return min(any_matches)


while True:
    try:
        result = discrete_logarithm(*(int(i) for i in input().split(" ")))
        if result is None:
            print("no solution\n")
        else:
            print(f"{result}\n")
    except:
        break