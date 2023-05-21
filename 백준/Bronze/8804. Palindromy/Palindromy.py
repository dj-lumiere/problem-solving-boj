# 8804 Palindromy


def check_palindrome(target: str) -> bool:
    start = 0
    end = len(target) - 1
    while start < end:
        if target[start] != target[end]:
            return False
        start += 1
        end -= 1
    return True


Z = int(input())
for _ in range(Z):
    S = input()
    if check_palindrome(S):
        print(1)
    else:
        print(2)
