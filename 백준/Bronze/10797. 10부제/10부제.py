# 10797 10부제

N = int(input())
print(sum([i == N for i in list(map(int, input().split(" ")))]))