def eea(a:int, b:int, d:int) -> list[int]:
    # (x(0),y(0)) = (1,0), (x(1),y(1)) = (0,1)
    x_y_seq_memo:list[list[int]] = [[1,0],[0,1]]
    # r(0) = a, r(1) = b
    r_memo:list[int] = [a,b]
    q_i:int = 0
    i:int = 1
    while True:
        if r_memo[i%2]==d:
            break
        else:
            i += 1
            # q(i+2) = r(i)//r(i+1)
            q_i = r_memo[(i-2)%2] // r_memo[(i-1)%2]
            # r(i+2) = r(i)//r(i+1)
            r_memo[i%2]=r_memo[(i-2)%2] % r_memo[(i-1)%2]
            # (x(i+2),y(i+2))=(x(i)-x(i+1)*q(i+2),y(i)-y(i+1)*q(i+2))
            for j in range(2):
                x_y_seq_memo[i%2][j]=x_y_seq_memo[(i-2)%2][j]-x_y_seq_memo[(i-1)%2][j]*q_i
    return x_y_seq_memo[i%2]

def gcd(x:int, y:int) -> int:
    x, y = max(x,y), min(x,y)
    if x%y:
        return gcd(y, x%y)
    else:
        return y

def cain_calendar(m, n, x, y) -> int:
    if m == 1 and n == 1:
        return 1
    #X = x(mod m), X = y(mod n)인 X찾기
    if gcd(m,n) == 1:
        # 중국인의 나머지 정리
        # sum(a*n*s)
        mod = (x*n*eea(n,m,1)[0]+y*m*eea(m,n,1)[0])%(m*n)
        if not mod:
            return m*n
        else:
            return mod
    else:
        g = gcd(m,n)
        l = m*n//g
        if abs(x-y) % g:
            return -1
        else:
            p,q = eea(m,n,g)
            mod_candidate = ((x*n*q+y*m*p)//g) % (l)
            if not mod_candidate:
                return l
            else:
                return mod_candidate

test_case = int(input())
for i in range(test_case):
    m,n,x,y = list(map(int, input().split(" ")))
    print(cain_calendar(m,n,x,y))