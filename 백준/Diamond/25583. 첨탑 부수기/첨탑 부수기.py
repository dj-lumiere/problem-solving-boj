from sys import stdin


def input():
    return stdin.readline().strip()


def precompute_euler_phi(M, limit):
    eulerphi = {}
    prime_flags = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if not prime_flags[i]:
            continue
        prime_flags[i * 2 : limit + 1 : i] = [False] * (limit // i - 1)
    current = M
    result = M
    while current != 1:
        is_prime = True
        tmp = current
        for i in range(2, limit + 1):
            if not prime_flags[i]:
                continue
            if current % i != 0:
                continue
            result *= i - 1
            result //= i
            while tmp % i == 0:
                tmp //= i
            is_prime = False
        if tmp != 1:
            result *= tmp - 1
            result //= tmp
        eulerphi[current] = result
        current = result
    return eulerphi


def is_excessive(base: int, exp: int, threshold: int):
    result = 1
    while exp:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
        if result >= threshold or base >= threshold:
            return True
    return False


def power_tower(eulerphi, tower, index: int, MOD: int):
    global is_excessive_at_next
    if len(tower) - index == 1 or MOD == 1:
        return tower[index]
    euler_phi_mod = eulerphi[MOD]
    sub_result = power_tower(eulerphi, tower, index + 1, euler_phi_mod)
    base, exp = tower[index], sub_result
    if is_excessive_at_next:
        exp += euler_phi_mod
    # print(f"{index=} {MOD=} {tower[index:]=} {base=} {exp=} {is_excessive(base, exp, MOD)=}")
    if not is_excessive_at_next:
        is_excessive_at_next = is_excessive(base, exp, MOD)
    return pow(base, exp, MOD)

def convert_to_digit(char):
    if char.isdigit():
        return int(char)
    if char.isupper():
        return 10 + ord(char) - ord("A")
    if char.islower():
        return 36 + ord(char) - ord("a")
    return -1

global is_excessive_at_next
is_excessive_at_next = False


N, M = map(int, input().split(" "))
seed = input()
eulerphi = precompute_euler_phi(M, 10**5)
tower = []
for i, v in enumerate(reversed(range(1, N+1))):
    if i >= len(eulerphi):
        break
    if v == 1:
        tower.append(1)
        break
    tower.append(sum(convert_to_digit(seed[v*j%10]) for j, _ in enumerate(seed))*v)
is_excessive_at_next = False
for i, v in enumerate(tower):
    if v == 1:
        tower = tower[:i]
        break
if not tower and M != 1:
    print(1)
    exit(0)
if M == 1:
    print(0)
    exit(0)
print(power_tower(eulerphi, tower, 0, M) % M)