# 5565 영수증

total_price = int(input())
readable_price = [int(input()) for _ in range(9)]
print(total_price - sum(readable_price))