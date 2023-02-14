from sys import stdin

def eea(a:int, b:int, d:int) -> int:
    x_y_seq_memo:list[list[int]] = [[1,0],[0,1]]
    r_memo:list[int] = [a,b]
    q_i:int = 0
    i:int = 2
    while True:
        q_i = r_memo[(i-2)%2] // r_memo[(i-1)%2]
        r_memo[i%2]=r_memo[(i-2)%2] % r_memo[(i-1)%2]
        for j in range(2):
            x_y_seq_memo[i%2][j]=x_y_seq_memo[(i-2)%2][j]-x_y_seq_memo[(i-1)%2][j]*q_i
        if r_memo[i%2]==d:
            break
        else:
            i += 1
    return x_y_seq_memo[i%2][0]

M = int(input())
expectation = 0
modulo = 1000000007
for i in range(M):
    N, S = list(map(int, stdin.readline().rstrip().split(" ")))
    expectation += S * eea(N, modulo, 1)
    expectation %= modulo
print(expectation)