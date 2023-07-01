# 28203 자석

N, K = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
best_index_forward_north = 0
best_energy_forward_north = a[0] - a[1] - K
for index, value in enumerate(a):
    if index < 2:
        continue
    if a[best_index_forward_north] < a[index - 1] + K * (
        index - 1 - best_index_forward_north
    ):
        best_index_forward_north = index - 1
    best_energy_forward_north = max(
        best_energy_forward_north,
        a[best_index_forward_north] - a[index] - K * (index - best_index_forward_north),
    )
a.reverse()
best_index_forward_south = 0
best_energy_forward_south = a[0] - a[1] - K
for index, value in enumerate(a):
    if index < 2:
        continue
    if a[best_index_forward_south] < a[index - 1] + K * (
        index - 1 - best_index_forward_south
    ):
        best_index_forward_south = index - 1
    best_energy_forward_south = max(
        best_energy_forward_south,
        a[best_index_forward_south] - a[index] - K * (index - best_index_forward_south),
    )
print(max(best_energy_forward_north, best_energy_forward_south))