def adding_reverse(a:int, modulo:int):
    return (-1 * a) % modulo

def multiplying_reverse(a:int, modulo:int):
    if gcd(a, modulo) != 1:
        return -1
    else:
        return eea(a, modulo, 1) % modulo

def gcd(x:int, y:int) -> int:
    x, y = max(x,y), min(x,y)
    if x%y:
        return gcd(y, x%y)
    else:
        return y

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

N, A = list(map(int, input().split(" ")))
print(f'{adding_reverse(A, N)} {multiplying_reverse(A, N)}')
