# A번 - 찬반투표

from collections import Counter

N = int(input())
vote_count = Counter(map(int, input().split(" ")))

if vote_count[0] * 2 >= N:
    print("INVALID")
elif vote_count[1] <= vote_count[-1]:
    print("REJECTED")
else:
    print("APPROVED")
