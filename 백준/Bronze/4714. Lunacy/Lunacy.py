# 4714 Lunacy
from decimal import Decimal

while True:
    x = Decimal(input())
    if x < 0:
        break
    print(f"Objects weighing {x:.2f} on Earth will weigh {x*Decimal('0.167'):.2f} on the moon.")