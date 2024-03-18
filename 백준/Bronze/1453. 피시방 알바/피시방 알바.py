from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))
print(sum(v - 1 for i, v in A.items()))