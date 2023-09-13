# 4890 Tiles of Tetris, NOT!
from math import lcm

while True:
    a, b = map(int, input().split(" "))
    if not any((a, b)):
        break
    l = lcm(a, b)
    print(l * l // a // b)