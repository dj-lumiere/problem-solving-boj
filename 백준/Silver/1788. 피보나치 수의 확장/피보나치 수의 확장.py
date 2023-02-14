def fib_ext(N: int) -> int:
    memo:list[int] = [0,1]
    if N >= 2:
        for i in range(2, N+1):
            memo[i%2] = (memo[(i-1)%2]+memo[(i-2)%2]) % 1000000000
    elif N < 0:
        for i in range(-1, N-1, -1):
            memo[i%2] = sign((memo[(i+2)%2]-memo[(i+1)%2]))*(abs((memo[(i+2)%2]-memo[(i+1)%2])) % 1000000000)
    return memo[N%2]

def sign(x: int) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

N = int(input())
fib_value = fib_ext(N)

print(sign(fib_value))
print(abs(fib_value))