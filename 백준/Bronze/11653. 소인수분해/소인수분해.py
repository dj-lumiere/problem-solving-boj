def find_prime(a:int) -> list[bool]:
    if a == 1:
        return []
    else:
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

def find_prime_factor(a:int) -> dict[int, int]:
    if a == 1:
        return {1:1}
    else:
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

a= int(input())
if a != 1:
    factorized = find_prime_factor(a)
    for i in factorized:
        for j in range(factorized[i]):
            print(i)