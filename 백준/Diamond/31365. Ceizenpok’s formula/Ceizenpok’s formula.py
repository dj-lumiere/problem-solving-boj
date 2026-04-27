# 14854 이항 계수 6


def n_ary_change(x, n) -> list[int]:
    next_x = x
    change_list = []
    while next_x:
        change_list.append(next_x % n)
        next_x //= n
    return change_list


def extract_primes_from_sieve(limit: int) -> list[int]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit ** 0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2: limit + 1: i] = [False] * (limit // i - 1)
    return [i for i, v in enumerate(is_prime) if v]


def get_prime_factors(value: int, primes: list[int]) -> list[int]:
    prime_factors = []
    for i in primes:
        if i * i > value:
            break
        if value % i:
            continue
        while value % i == 0:
            prime_factors.append(i)
            value //= i
    if value != 1:
        prime_factors.append(value)
    return prime_factors


def factorize(value: int) -> dict[int, int]:
    prime_factors = get_prime_factors(value, prime_list)
    factorized_dict = dict()
    for factor in prime_factors:
        factorized_dict[factor] = factorized_dict.get(factor, 0) + 1
    return factorized_dict


def power_count_in_x_factorial(x: int, a: int) -> int:
    answer = 0
    answer_sub = 1
    next_factor = a
    while answer_sub:
        answer_sub = x // next_factor
        next_factor *= a
        answer += answer_sub
    return answer


def x_factorial_with_coprime(x: int, a: int, b: int) -> int:
    coprime_accumulated_product = [1]
    for i in range(1, a ** b + 1):
        if not i % a:
            coprime_accumulated_product.append(coprime_accumulated_product[-1])
        else:
            coprime_accumulated_product.append(coprime_accumulated_product[-1] * i % a ** b)
    answer = 1
    next_factor = 1
    while next_factor <= x:
        batches, leftover = divmod(x // next_factor, a ** b)
        answer *= pow(coprime_accumulated_product[a ** b], batches, a ** b)
        answer *= coprime_accumulated_product[leftover]
        answer %= a ** b
        next_factor *= a
    return answer


# 뤼카 정리 활용
prime_list = extract_primes_from_sieve(1000)
a, b, m = map(int, input().split())
m_factors = factorize(m).items()
m_list = [k ** v for k, v in m_factors]
s_list = [pow(m // i, -1, i) for i in m_list]
n_list = [m // i for i in m_list]
mods = []
for k, v in m_factors:
    a_fact_mod_kv = x_factorial_with_coprime(x=a, a=k, b=v)
    b_fact_mod_kv = x_factorial_with_coprime(x=b, a=k, b=v)
    a_minus_b_fact_mod_kv = x_factorial_with_coprime(x=a - b, a=k, b=v)
    power_k_count = power_count_in_x_factorial(a, k) - power_count_in_x_factorial(a - b, k) - power_count_in_x_factorial(b, k)
    if power_k_count >= v:
        power_k_count = v
    aCb_mod_kv = a_fact_mod_kv * pow(b_fact_mod_kv, -1, k ** v) * pow(a_minus_b_fact_mod_kv, -1, k ** v) * pow(k, power_k_count) % (
            k ** v)
    mods.append(aCb_mod_kv)
answer = sum(m_i * n_i * s_i for m_i, n_i, s_i in zip(mods, n_list, s_list)) % m
print(answer)
#print(m_factors, m_list, mods)