# 10942 팰린드롬?

from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
sequence = list(map(int, input().split(" ")))
odd_length_palindrome = [[] for _ in range(N)]
even_length_palindrome = [[] for _ in range(N - 1)]
for i in range(N):
    is_palindrome = True
    start = i
    end = i
    while start >= 0 and end < N:
        if not is_palindrome:
            pass
        elif sequence[start] != sequence[end]:
            is_palindrome = False
        start -= 1
        end += 1
        odd_length_palindrome[i].append(is_palindrome)
for i in range(N - 1):
    is_palindrome = True
    start = i
    end = i + 1
    while start >= 0 and end < N:
        if not is_palindrome:
            pass
        elif sequence[start] != sequence[end]:
            is_palindrome = False
        start -= 1
        end += 1
        even_length_palindrome[i].append(is_palindrome)

M = int(input())
for _ in range(M):
    start, end = map(int, input().split(" "))
    length = end - start + 1
    mid = (start + end) // 2 - 1
    half_length = mid + 1 - start

    if length % 2:
        print(int(odd_length_palindrome[mid][half_length]))
    else:
        print(int(even_length_palindrome[mid][half_length]))