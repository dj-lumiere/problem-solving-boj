# 17466 N! mod P (1)

N, P = list(map(int, input().split(" ")))
answer:int = 1
for i in range(1, N+1):
    answer = answer * i % P
print(answer)