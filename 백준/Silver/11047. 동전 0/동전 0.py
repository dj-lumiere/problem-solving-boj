from collections import deque

def coin(coin_value : deque[int], target_value : int) -> int:
    coin_count:int = 0
    for i in coin_value:
        if target_value >= i:
            coin_count += target_value // i
            target_value = target_value % i
    return coin_count

N, K = list(map(int, input().split(" ")))
a_i = deque()
for i in range(N):
    a_i.appendleft(int(input()))

print(coin(a_i,K))