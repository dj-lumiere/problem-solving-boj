# 15328 산타의 선물

from decimal import Decimal
from sys import stdin

T = int(stdin.readline().strip())
for _ in range(T):
    time_limit: int = int(stdin.readline().strip())
    position_list: list[tuple[Decimal, Decimal, Decimal]] = [
        tuple(map(Decimal, stdin.readline().strip().split(" "))) for _ in range(4)
    ]
    current_position: tuple[Decimal, Decimal, Decimal] = (
        Decimal(0),
        Decimal(0),
        Decimal(0),
    )
    time_to_spend: Decimal = Decimal(0)
    for i, next_position in enumerate(position_list):
        time_to_spend_sub: Decimal = sum(
            [(next_position[j] - current_position[j]) ** 2 for j in range(3)]
        )
        time_to_spend += time_to_spend_sub.sqrt()
        current_position = next_position
    if time_to_spend > time_limit:
        print("NO")
    else:
        print("YES")