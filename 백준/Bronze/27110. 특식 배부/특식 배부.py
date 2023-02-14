N = int(input())
chicken_counts = list(map(int, input().split(" ")))
result = 0

def sol(soldiers: int, chickens: int) -> int:
    if soldiers <= chickens:
        return soldiers
    else:
        return chickens

for i in chicken_counts:
    result += sol(i, N)

print(result)