# 29702 이상한 호텔의 송이


def find_minimal_path(target: int):
    current_floor = target.bit_length()
    current_room = target
    path = []
    while current_floor > 0:
        room_order_in_current_floor = current_room - (1 << (current_floor - 1)) + 1
        path.append(f"{current_floor}{room_order_in_current_floor:0>18}")
        current_floor -= 1
        current_room >>= 1
    return path


T = int(input())
for _ in range(T):
    N = int(input())
    print(*find_minimal_path(N), sep="\n")
