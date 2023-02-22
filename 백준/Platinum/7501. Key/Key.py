# 7501 Key

# (K-1)!이 K^2로 나누어떨어지지 않는다는 이야기는 K의 인수 중에 2~K-1이 전부 없다는 이야기 <=> K는 소수
# A<=K<=B인 K 중 소수인 것들 찾기

# if n < 3,825,123,056,546,413,051, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, and 23 (from wikipedia)
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]


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


A, B = list(map(int, input().lstrip().rstrip().split(" ")))
possible_values = []
for i in range(A, B + 1):
    if i % 2:
        if is_prime(i):
            possible_values.append(i)
        # 9는 예외적으로 조건을 만족하므로 possible_values에 
        elif i == 9:
            possible_values.append(i)
print(*possible_values, sep=" ")
