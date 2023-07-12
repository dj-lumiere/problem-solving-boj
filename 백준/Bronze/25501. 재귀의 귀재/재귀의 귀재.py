# 25501 재귀의 귀재


def sol(target) -> tuple[int, int]:
    l = 0
    r = len(target) - 1
    called_count = 0
    is_palindrome = 1
    while l < r:
        called_count += 1
        if target[l] != target[r]:
            is_palindrome = 0
            break
        l += 1
        r -= 1
    if is_palindrome:
        called_count += 1
    return (is_palindrome, called_count)


N = int(input())
for _ in range(N):
    target_string = input()
    print(*sol(target_string))