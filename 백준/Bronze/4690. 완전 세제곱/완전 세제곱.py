# 4690 완전 세제곱

from itertools import product

for a, b, c, d in product(range(2, 101), repeat=4):
    if a**3 == b**3 + c**3 + d**3 and b <= c <= d:
        print(f"Cube = {a}, Triple = ({b},{c},{d})")