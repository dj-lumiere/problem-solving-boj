# 18110 solved.ac

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input().strip())
level_opinions = []
for _ in range(n):
    level_opinions.append(int(input().strip()))

if not n:
    print("0")
else:
    level_opinions.sort()
    cutoff_quotient, cutoff_mod = divmod(3 * n, 20)
    cutoff = cutoff_quotient
    if cutoff_mod * 2 >= 20:
        cutoff += 1
    if cutoff == 0:
        cutoff_sum = sum(level_opinions)
    else:
        cutoff_sum = sum(level_opinions[cutoff:-cutoff])
    cutoff_people = n - 2 * cutoff
    result, mod = divmod(cutoff_sum, cutoff_people)
    if mod * 2 >= cutoff_people:
        result += 1
    print(f"{result}")
