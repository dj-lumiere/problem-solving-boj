# 30089 새로운 문자열 만들기

from sys import stdin


def input():
    return stdin.readline().strip()


def is_palindrome(target: str):
    start = 0
    end = len(target) - 1
    while start + 1 <= end:
        if target[start] != target[end]:
            return False
        start += 1
        end -= 1
    return True


def shortest_palindrome_with_prefix(prefix: str):
    if is_palindrome(prefix):
        return prefix
    for i in range(1, len(prefix)):
        result_sub = prefix + (prefix[:i])[::-1]
        if is_palindrome(result_sub):
            return result_sub


T = int(input())
for _ in range(T):
    word = input()
    print(shortest_palindrome_with_prefix(word))