squares = [0 for _ in range(10**6+1)]
for i in range(1, 10**6+1, 2):
	squares[i] = i**2+(i-1)**2
for i in range(2, 10**6+1, 2):
	squares[i] = i*(i-1)*2
n, k = map(int, input().split())
answer = 0
for i in range(1, n+1):
	answer += squares[n+1-i]*pow(k, i, 10**9+7)
answer %= 10**9+7
print(answer)