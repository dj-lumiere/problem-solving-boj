a, b = map(int, input().split(" "))
print(min(a, b) if a&1 and b&1 else 0)