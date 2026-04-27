# 29782 ASCII Art
# i를 이분탐색으로 구한 뒤, 그 뒤의 세부적인 레터를 구한다.


def i_th_set_letter_count(i):
    return 26 * i * (i + 1) // 2


def find_set_count_offset(n):
    start = 0
    end = n + 1
    while start + 1 < end:
        mid = (start + end) // 2
        letter_count = i_th_set_letter_count(mid)
        if letter_count > n:
            end = mid
        else:
            start = mid
    return start, n - i_th_set_letter_count(start)


def find_letter(n):
    set_count, offset = find_set_count_offset(n)
    return chr(ord("A") + offset // (set_count + 1))


T = int(input())
for i in range(1, T + 1):
    n = int(input()) - 1
    print(f"Case #{i}: {find_letter(n)}")