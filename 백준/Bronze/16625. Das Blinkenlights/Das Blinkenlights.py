# 16625 Das Blinkenlights
from math import lcm

p, q, s = map(int, input().split(" "))
print("yes" if s >= lcm(p, q) else "no")