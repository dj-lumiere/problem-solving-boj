def find_prime(a:int) -> list[bool]:
    finder_limit = int(a**.5)+1
    prime_list:list[bool] = [True for i in range(0, finder_limit+1)]
    prime_list[0] = False
    prime_list[1] = False
    for x in range(1, int(finder_limit**.5)+1):
        if prime_list[x]:
            prime_list[x:finder_limit+1:x] = [False] * (finder_limit//x)
            prime_list[x] = True
        else:
            continue
    return prime_list

def factorize(a:int) -> dict[int, int]:
    factorized_dict = dict()
    prime_list = find_prime(a)
    next_factor = a
    for i in range(0, int(a**.5)+1):
        if prime_list[i] and not next_factor % i:
            factorized_dict[i] = 0
            while not (next_factor % i):
                factorized_dict[i] += 1
                next_factor = next_factor // i
    if next_factor != 1:
        factorized_dict[next_factor] = 1
    return factorized_dict

N = int(input())

for i in range(N):
    target = int(input())
    factorized_dict = factorize(target)
    for i in factorized_dict:
        print(f"{i} {factorized_dict[i]}")