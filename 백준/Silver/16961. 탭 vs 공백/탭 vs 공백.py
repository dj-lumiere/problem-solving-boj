# 16961 탭 vs 공백

import os

tokens = iter(os.read(0, os.fstat(0).st_size).split())
N = int(next(tokens))
hotel_reserve_tab = [0 for _ in range(367)]
hotel_reserve_space = [0 for _ in range(367)]
longest_period = 0

for _ in range(N):
    c, s, e = next(tokens), int(next(tokens)), int(next(tokens))
    if c == b'T':
        for i in range(s, e + 1):
            hotel_reserve_tab[i] += 1
    if c == b'S':
        for i in range(s, e + 1):
            hotel_reserve_space[i] += 1
    longest_period = max(longest_period, e - s + 1)

max_booked_quantity = max(tab + space for tab, space in zip(hotel_reserve_tab, hotel_reserve_space))
max_booked_quantity_no_fight = max(
    tab + space if tab == space else 0 for tab, space in zip(hotel_reserve_tab, hotel_reserve_space))
answer = [0, max_booked_quantity, 366, max_booked_quantity_no_fight, longest_period]
for tab, space in zip(hotel_reserve_tab[1:], hotel_reserve_space[1:]):
    if tab or space:
        answer[0] += 1
    if tab != space or not tab or not space:
        answer[2] -= 1

os.write(1, "\n".join(map(str, answer)).encode())