# 1107 리모컨
from sys import stdin, stdout

input = stdin.readline
print = stdout.write
N = int(input())
M = int(input())
failed_button = []
if M:
    failed_button = list(map(int, input().split(" ")))
INVALID = 1_000_000_000_000
button_minimal_press = [INVALID for _ in range(1000001)]
for i in range(1000001):
    if not any(str(j) in str(i) for j in failed_button):
        button_minimal_press[i] = len(str(i)) + abs(N - i)
plus = N - 100 if N >= 100 else INVALID
minus = 100 - N if N <= 100 else INVALID
print(f"{min(plus, minus, *button_minimal_press)}")