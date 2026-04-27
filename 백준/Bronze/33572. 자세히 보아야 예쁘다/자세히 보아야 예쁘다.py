n, m = map(int, input().split())

a = list(map(int, input().split()))

print("OUT" if sum(a)-n<m else "DIMI")