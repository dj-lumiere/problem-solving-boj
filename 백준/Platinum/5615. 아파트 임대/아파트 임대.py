# 5615 아파트 임대

# 2(2xy+x+y)+1 = (2x+1)(2y+1)
# 2S+1이 소수가 아닌지 체크

# if n < 4,759,123,141, it is enough to test a = 2, 7, and 61 (from wikipedia)
prime_list = [2, 7, 61]
def powmod(a:int, b:int, m:int) -> int:
    result:int = 1
    next_b:int = b
    while b > 0:
        if b % 2:
            result = (result*a) % m
        b //= 2
        a = a * a % m
    return result
def is_prime(n: int):
    if n in prime_list:
        return True
    if n == 1 or n % 2 == 0:
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for a in [2, 7, 61]:
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y

        if x != 1:
            return False

    return True

T = int(input())
impossible_cases = 0
for _ in range(T):
    testing = 2*int(input())+1
    if is_prime(testing):
        impossible_cases += 1
print(impossible_cases)