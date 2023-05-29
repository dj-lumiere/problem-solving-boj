# 28086 미소녀 컴퓨터 파루빗토 쨩

from sys import stdin, stdout
from re import split
from math import floor

input = stdin.readline
print = stdout.write

INVALID_RESULT = -(8**10)
INT_MAX = 8**9
INT_MIN = -(8**9)

formula = split(r"(\+|-|\*-|/-|\*|/)", input().strip())
result = INVALID_RESULT
if not formula[0]:
    formula.pop(0)
    formula.pop(0)
    formula[0] = "-" + formula[0]
if formula[1] == "+":
    result = int(formula[0], base=8) + int(formula[2], base=8)
elif formula[1] == "-":
    result = int(formula[0], base=8) - int(formula[2], base=8)
elif formula[1] == "*-":
    result = int(formula[0], base=8) * int(formula[2], base=8) * -1
elif formula[1] == "/-" and formula[2] != "0":
    result = floor(int(formula[0], base=8) / int(formula[2], base=8) * -1)
elif formula[1] == "*":
    result = int(formula[0], base=8) * int(formula[2], base=8)
elif formula[1] == "/" and formula[2] != "0":
    result = floor(int(formula[0], base=8) / int(formula[2], base=8))
if result != INVALID_RESULT:
    print(f"{result:o}")
else:
    print("invalid")