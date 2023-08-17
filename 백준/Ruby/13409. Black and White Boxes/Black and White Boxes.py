# 13409 Black and White Boxes
from sys import stdin


def input():
    return stdin.readline().strip()


def find_box_number(box_configuration: str) -> int:
    if not box_configuration:
        return 0
    box_list = [1 if i == "B" else -1 for i in box_configuration]
    sign = 1
    result = 0
    multiplier = 1 << 40
    # 처음이 W면 반대로 생각
    if box_list[0] == -1:
        box_list = [-i for i in box_list]
        sign = -1
    # 첫번째 색상 변경을 기준으로 생각
    first_color_change = -1
    for i, v in enumerate(box_list):
        if i == 0:
            continue
        if v != box_list[i - 1]:
            first_color_change = i - 1
            break
    # 색상 변경이 없을 경우 길이가 값이 됨
    if first_color_change == -1:
        result = multiplier * len(box_configuration) * sign
        return result
    # 색상 변경이 있을 경우 색상 변경 이후로는 0.5배씩 등비수열처럼 곱해짐
    result = multiplier * first_color_change
    box_list = box_list[first_color_change:]
    result += sum((multiplier >> i) * v for i, v in enumerate(box_list))
    return result * sign


def register_combination(sums_dict, status, size, numbers, offset):
    total_value, total_box_count = 0, 0
    for i in range(size):
        if not (status >> i) & 1:
            continue
        total_value += numbers[offset + i][0]
        total_box_count += numbers[offset + i][1]
    if total_value not in sums_dict or total_box_count > sums_dict[total_value]:
        sums_dict[total_value] = total_box_count


# 합이 0이 되는 조합 중 상자의 갯수를 가장 많이 가져갈 수 있는 조합 찾기
def find_max_box_number(numbers) -> int:
    n = len(numbers)
    n1, n2 = n // 2, n - n // 2
    sums_left = {}
    sums_right = {}
    for status in range(1, 1 << n1):
        register_combination(sums_left, status, n1, numbers, 0)
    for status in range(1, 1 << n2):
        register_combination(sums_right, status, n2, numbers, n1)
    max_box_count = 0
    for value, box_count in sums_left.items():
        if -value in sums_right:
            max_box_count = max(max_box_count, box_count + sums_right[-value])
    return max_box_count


def main():
    N = int(input())
    box_numbers = []
    for _ in range(N):
        box_configuration = input()
        box_numbers.append(
            (
                find_box_number(box_configuration),
                len(box_configuration),
            )
        )
    box_numbers.sort(key=lambda x: (x[0], -x[1]))
    result = find_max_box_number(box_numbers)
    print(result)


main()