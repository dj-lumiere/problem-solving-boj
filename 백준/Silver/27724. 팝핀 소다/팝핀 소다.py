# A번 - 팝핀 소다
from math import log2

N, M, K = list(map(int, input().split(" ")))

max_win_count = int(log2(N))
player_normal_win_count = int(log2(K))

print(min(max_win_count, player_normal_win_count + M))