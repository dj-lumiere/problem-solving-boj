# 10707 수도요금

A, B, C, D, P = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)

print(min(A * P, B + D * (max(P - C, 0))))