# 20454 Кампус


def find_entrance_number_and_remainder(
    n: int, x: int, y: int, k: int, target: int
) -> tuple[int, int]:
    entrance_capacity = n * y - (n // k) * (y - x)
    q, r = divmod(target - 1, entrance_capacity)
    return (q, r)


def find_floor_capacity(x: int, y: int, k: int, target: int) -> int:
    return target * y - (target // k) * (y - x)


def find_floor_number(n: int, x: int, y: int, k: int, target: int) -> int:
    low = 0
    high = n
    while low + 1 < high:
        mid = (low + high) // 2
        capacity_until_mid_floor = find_floor_capacity(x, y, k, mid)
        if capacity_until_mid_floor > target:
            high = mid
        else:
            low = mid
    return low


n, k, x, y = map(int, input().split(" "))
q = int(input())
queries = list(map(int, input().split(" ")))
for v in queries:
    entrance_number, remainder = find_entrance_number_and_remainder(n, x, y, k, v)
    floor_number = find_floor_number(n, x, y, k, remainder) + 1
    print(floor_number)