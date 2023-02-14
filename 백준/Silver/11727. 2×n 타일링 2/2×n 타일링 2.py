n = int(input())

def tiling(size:int) -> int:
    memo = [0,0,0]
    for i in range(1, size + 1):
        if i == 1:
            memo[i%3] = 1
        elif i == 2:
            memo[i%3] = 3
        elif i == 3:
            memo[i%3] = 5
        else:
            memo[i%3] = (2*memo[(i-3)%3] + 3*memo[(i-2)%3])%10007
    return memo[i%3]

print(tiling(n))