# 13618 RSA

# N = A*B 형태로 나누어짐
# D = E**-1 (mod phi(N))
# M=C**D (mod N)

# 10**(9*.5)까지 소수 계산
# a까지의 소수를 찾기
def find_prime(a: int) -> list[int]:
    if a == 1:
        return []
    else:
        finder_limit = a
        prime_list: list[bool] = [True for i in range(0, finder_limit + 1)]
        prime_list[0] = False
        prime_list[1] = False
        for x in range(1, int(finder_limit**0.5) + 1):
            if prime_list[x]:
                prime_list[x : finder_limit + 1 : x] = [False] * (finder_limit // x)
                prime_list[x] = True
            else:
                continue
        prime_list2 = [i for (i, j) in enumerate(prime_list) if j]
        return prime_list2


# 확장된 유클리드 호제법
def eea(a: int, b: int, d: int) -> list[int]:
    # (x(0),y(0)) = (1,0), (x(1),y(1)) = (0,1)
    x_y_seq_memo: list[list[int]] = [[1, 0], [0, 1]]
    # r(0) = a, r(1) = b
    r_memo: list[int] = [a, b]
    q_i: int = 0
    i: int = 2
    while True:
        # q(i+2) = r(i)//r(i+1)
        q_i = r_memo[(i - 2) % 2] // r_memo[(i - 1) % 2]
        # r(i+2) = r(i)//r(i+1)
        r_memo[i % 2] = r_memo[(i - 2) % 2] - q_i * r_memo[(i - 1) % 2]
        # (x(i+2),y(i+2))=(x(i)-x(i+1)*q(i+2),y(i)-y(i+1)*q(i+2))
        for j in range(2):
            x_y_seq_memo[i % 2][j] = (
                x_y_seq_memo[(i - 2) % 2][j] - x_y_seq_memo[(i - 1) % 2][j] * q_i
            )
        if r_memo[i % 2] == d:
            break
        else:
            i += 1
    return x_y_seq_memo[i % 2]


N, E, C = list(map(int, input().split(" ")))

P: int = 0
Q: int = 0
prime_list = find_prime(int(10**4.5))
for i in prime_list:
    if not N % i:
        P, Q = i, N // i
euler_phi = (P - 1) * (Q - 1)

# D 구하기
D = eea(E, euler_phi, 1)[0] % euler_phi
# M 구하기
M = pow(C, D, N)
print(M)
