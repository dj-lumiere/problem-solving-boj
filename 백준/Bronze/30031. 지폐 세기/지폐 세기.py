# 30031 지폐 세기

paper_size_to_price_dict = {136: 1000, 142: 5000, 148: 10000, 154: 50000}
total_money = 0
n = int(input())
for _ in range(n):
    width, _ = map(int, input().split(" "))
    total_money += paper_size_to_price_dict[width]
print(total_money)