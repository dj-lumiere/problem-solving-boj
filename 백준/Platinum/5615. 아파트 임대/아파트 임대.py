# 5615 아파트 임대

# 2(2xy+x+y)+1 = (2x+1)(2y+1)
# 2S+1이 소수가 아닌지 체크

# if n < 4,759,123,141, it is enough to test a = 2, 7, and 61 (from wikipedia)
prime_list = [2, 7, 61]
def is_prime(n: int):
    # prime_list의 원소들을 미리 소수로 처리
    if n in prime_list:
        return True
    # 1과 짝수는 소수가 아님
    if n == 1 or n % 2 == 0:
        return False
    # (n-1) = 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    y = 1
    # 소수 리스트를 참조하여 소수 판별
    for i in prime_list:
        x = pow(i, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x + 1 != n:
                return False
            x = y
        if y != 1:
            return False
    return True

T = int(input())
impossible_cases = 0
for _ in range(T):
    testing = 2*int(input())+1
    if is_prime(testing):
        impossible_cases += 1
print(impossible_cases)
