# 30034 Slice String

from re import split

N = int(input())
seperators = list()
seperators.extend(list(input().split(" ")))
M = int(input())
seperators.extend(list(input().split(" ")))
K = int(input())
mergers = []
mergers.extend(list(input().split(" ")))
seperators = set(seperators)
mergers = set(mergers)
seperators = seperators.difference(mergers)
seperators.add(" ")
S = int(input())
target = input()
target_seperated = split("|".join(seperators), target)
target_seperated = [i for i in target_seperated if i]
print(*target_seperated, sep="\n")