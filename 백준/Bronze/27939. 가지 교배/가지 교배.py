# 27939 가지 교배

from sys import stdin
from typing import Callable

N: int = int(stdin.readline().strip())
gaji_to_boolean: Callable[[str], bool] = lambda x: x == "P"
gaji_list_element_to_boolean: Callable[[str], bool] = lambda x: gaji_species[int(x) - 1]
gaji_species: list[bool] = list(
    map(gaji_to_boolean, stdin.readline().strip().split(" "))
)
m, k = map(int, stdin.readline().strip().split(" "))
purple_anyway_list: list[bool] = []
for _ in range(m):
    a_ij: list[bool] = list(
        map(gaji_list_element_to_boolean, stdin.readline().strip().split(" "))
    )
    purple_anyway_list.append(not any(a_ij))
if any(purple_anyway_list):
    print("W")
else:
    print("P")