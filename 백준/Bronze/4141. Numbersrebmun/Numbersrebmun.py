# 4141 Numbersrebmun (4월 1일 스트릭 유지용)

from sys import stdin

N: int = int(stdin.readline().strip())


def string_to_keypad(input_string: str) -> list[int]:
    A: int = ord("A")
    # ABC:2, DEF:3, GHI:4, JKL:5, MNO:6, PQRS:7, TUV:8, WXYZ:9
    conversion_dict: str = "22233344455566677778889999"
    return [int(conversion_dict[ord(i.upper()) - A]) for i in input_string]


def palindrome_check(list_to_check: list[int]) -> bool:
    head_ptr: int = 0
    tail_ptr: int = -1
    list_len: int = len(list_to_check)
    while head_ptr < list_len + tail_ptr:
        if list_to_check[head_ptr] != list_to_check[tail_ptr]:
            return False
        else:
            head_ptr += 1
            tail_ptr -= 1
    return True


for _ in range(N):
    if palindrome_check(string_to_keypad(stdin.readline().strip())):
        print("YES")
    else:
        print("NO")