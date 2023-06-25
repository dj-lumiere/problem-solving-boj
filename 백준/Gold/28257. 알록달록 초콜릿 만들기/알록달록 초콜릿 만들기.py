# C번 - 알록달록 초콜릿 만들기
from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def find_line_number(index: int) -> int:
    start = 0
    end = 10**16 + 1
    while start + 1 < end:
        mid = (start + end) // 2
        if find_blue_count(mid) > index:
            end = mid
        else:
            start = mid
    return start


def find_blue_count(line_number: int) -> int:
    even_line = 0
    odd_line = 0
    if line_number % 2:
        odd_line, even_line = line_number // 2, line_number // 2 + 1
    else:
        odd_line, even_line = line_number // 2, line_number // 2
    odd_line_group, odd_line_residue = divmod(max(0, odd_line - 1), 3)
    even_line_group, even_line_residue = divmod(even_line, 3)
    blue_count_in_even_line = (
        3 * even_line_group**2 + ((even_line_group + 1) * 2 - 1) * even_line_residue
    )
    blue_count_in_odd_line = (
        3 * (odd_line_group**2 + odd_line_group)
        + ((odd_line_group + 1) * 2) * odd_line_residue
    )
    return blue_count_in_even_line + blue_count_in_odd_line


def find_blue_numbers_in_line(line_number: int) -> int:
    even_line = 0
    odd_line = 0
    if line_number % 2:
        odd_line, even_line = line_number // 2, line_number // 2 + 1
        odd_line_group, _ = divmod(max(0, odd_line - 1), 3)
        return (odd_line_group + 1) * 2 - 1 if line_number > 1 else 0
    else:
        odd_line, even_line = line_number // 2, line_number // 2
        even_line_group, _ = divmod(even_line, 3)
        return (even_line_group + 1) * 2


def find_number_at_index(line_number: int, index_in_line: int) -> int:
    even_line = 0
    odd_line = 0
    offset1 = find_starting_number_in_line(line_number)
    offset2 = 0
    if line_number % 2:
        odd_line, even_line = line_number // 2, line_number // 2 + 1
        _, odd_line_residue = divmod(max(0, odd_line - 1), 3)
        offset2 = odd_line_residue + 3 * index_in_line
    else:
        odd_line, even_line = line_number // 2, line_number // 2
        _, even_line_residue = divmod(even_line, 3)
        offset2 = even_line_residue + 3 * index_in_line
    return offset1 + offset2


def find_starting_number_in_line(line_number: int) -> int:
    return line_number * (line_number + 1) // 2 + 1


T = int(input())
for _ in range(T):
    target = int(input()) - 1
    line_number = find_line_number(target)
    line_index = target - find_blue_count(line_number)
    result = find_number_at_index(line_number, line_index)
    print(f"{result}\n")