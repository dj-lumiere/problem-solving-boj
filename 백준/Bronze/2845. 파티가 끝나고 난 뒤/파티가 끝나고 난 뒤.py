# 2845 파티가 끝나고 난 뒤

L, P = map(int, input().split(" "))
visitors = list(map(int, input().split(" ")))
print(*[i - L * P for i in visitors])