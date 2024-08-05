from itertools import product
from collections import Counter

t = int(input())
answers = []
for hh in range(t):
    a = int(input())
    scores = Counter(map(lambda x:-x, map(int, input().split())))
    answer = -scores.most_common(1)[0][0]
    answers.append(f"#{a} {answer}")
print(*answers, sep="\n")
