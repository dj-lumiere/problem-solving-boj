A, B, C = map(int, input().split())
print(max(abs(C-B), abs(B-A))-1)