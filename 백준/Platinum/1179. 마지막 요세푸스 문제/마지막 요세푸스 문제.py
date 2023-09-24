# 1179 마지막 요세푸스 문제
from functools import cache
from sys import setrecursionlimit

setrecursionlimit(1000000)

global function_call_count
function_call_count = 0


@cache
def sol(n, k):
    global function_call_count
    function_call_count += 1
    if n == 1:
        return 0
    if k == 1:
        return n - 1
    if 1 < n < k:
        return (sol(n - 1, k) + k) % n
    h = sol(n - n // k, k) - (n % k)
    if h < 0:
        return h + n
    return h + h // (k - 1)


n, k = map(int, input().split(" "))
print(sol(n, k) + 1)
