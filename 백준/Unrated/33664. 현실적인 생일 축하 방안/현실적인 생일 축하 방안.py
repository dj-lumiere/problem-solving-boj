B, N, M = map(int, input().split(" "))
item_name = []
item_cost = []
items_to_buy = []
for _ in range(N):
    i, p = input().split(" ")
    item_name.append(i)
    item_cost.append(int(p))
for _ in range(M):
    j = input()
    items_to_buy.append(j)
total_cost = sum([item_cost[item_name.index(item)] for item in items_to_buy])
print("unacceptable" if total_cost > B else "acceptable")
