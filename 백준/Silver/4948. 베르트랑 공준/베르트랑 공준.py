# 4948 베르트랑 공준


# a까지의 소수를 찾기
def prime_count(a: int) -> list[int]:
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
        prime_list_accumulated_sum = []
        for i, v in enumerate(prime_list):
            if i == 0:
                prime_list_accumulated_sum.append(0)
                continue
            prime_list_accumulated_sum.append(prime_list_accumulated_sum[-1] + v)
        return prime_list_accumulated_sum


prime_count_list = prime_count(123456 * 2)

while True:
    test = int(input())
    if test == 0:
        break
    print(prime_count_list[test * 2] - prime_count_list[test])