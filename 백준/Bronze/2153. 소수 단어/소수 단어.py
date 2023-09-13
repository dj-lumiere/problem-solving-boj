# 2153 소수 단어


def alphabet_to_number(letter):
    if "A" <= letter <= "Z":
        return ord(letter) - ord("A") + 27
    return ord(letter) - ord("a") + 1


def get_prime_sieve(limit: int) -> list[bool]:
    is_prime = [False, True] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2 : limit + 1 : i] = [False] * (limit // i - 1)
    return is_prime


prime_list = get_prime_sieve(1040)
number = sum(map(alphabet_to_number, list(input())))
print(f"It is {'' if prime_list[number] else 'not '}a prime word.")