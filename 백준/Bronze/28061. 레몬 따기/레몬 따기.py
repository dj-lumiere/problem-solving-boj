# 28061 레몬 따기

N = int(input())
A = [int(i) for i in input().split(" ")]
lemon_count = [
    max(0, lemon_quantity - (N - position)) for (position, lemon_quantity) in enumerate(A)
]
print(max(lemon_count))