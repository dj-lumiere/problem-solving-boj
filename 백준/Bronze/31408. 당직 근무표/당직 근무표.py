from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))
print("NO" if (N&1 and max(A.values()) > (N+1)//2) or (not N&1 and max(A.values()) > N // 2) else "YES")