# 11688 최소공배수 찾기


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
        prime_list2 = [i for i, j in enumerate(prime_list) if j]
        return prime_list2


prime_list = find_prime(10**6)


def find_prime_factor(a: int) -> dict[int, int]:
    if a == 1:
        return {1: 1}
    else:
        factorized_dict = dict()
        next_factor = a
        for j in prime_list:
            if j * j <= a and not next_factor % j:
                factorized_dict[j] = 0
                while not (next_factor % j):
                    factorized_dict[j] += 1
                    next_factor = next_factor // j
        if next_factor != 1:
            factorized_dict[next_factor] = 1
        return factorized_dict


def gcd(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    if x % y:
        return gcd(x % y, y)
    else:
        return y


def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)


# a, b, l 소인수분해하기
a, b, L = list(map(int, input().split(" ")))
a_b_dict = find_prime_factor(lcm(a, b))
l_dict = find_prime_factor(L)
for i, j in l_dict.items():
    if i not in a_b_dict:
        a_b_dict[i] = 0
for i, j in a_b_dict.items():
    if i not in l_dict:
        l_dict[i] = 0
c_dict = dict()

impossibility = False
for i, j in a_b_dict.items():
    # l과 비교해 a,b 쪽의 승수가 더 작으면 l쪽의 승수로 처리
    if l_dict[i] > j:
        c_dict[i] = l_dict[i]
    # l과 비교해 두개의 승수가 동률이면 0승으로 처리
    elif l_dict[i] == j:
        c_dict[i] = 0
    # l과 비교해 a,b 쪽의 승수가 더 크면 -1
    else:
        impossibility = True
        break

if impossibility:
    print(-1)
else:
    # 가능하면 모든 승수 다 곱해서 배출
    c = 1
    for i, j in c_dict.items():
        c *= i**j
    print(c)