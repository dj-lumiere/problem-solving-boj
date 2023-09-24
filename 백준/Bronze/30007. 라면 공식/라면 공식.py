# A번 - 라면 공식


def water_weight(coefficient, base_water_amount, quantity):
    return coefficient * (quantity - 1) + base_water_amount


N = int(input())
for _ in range(N):
    print(water_weight(*map(int, input().split(" "))))