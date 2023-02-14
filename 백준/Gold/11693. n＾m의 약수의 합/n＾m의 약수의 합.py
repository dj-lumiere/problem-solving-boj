# 소수 찾기
# a**.5까지의 소수를 찾음
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

# 소인수 찾기
# a**.5까지의 소수를 찾은 걸 체크해 소인수를 찾기.
def factorize(a:int) -> dict[int, int]:
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

def prime_power_divisor_sum(base: int, index: int, modulo: int) -> int:
    # (base ** (index+1) - 1) * ((base - 1) ** -1)
    if base == 1 or index == 0:
        return 1
    else:
        mod_dict = dict()
        mod = base % modulo
        binary_index = [(index + 1) // (2 ** i) % 2 for i in range(64)]
        final_mod = 1
        # mod_dict 세팅
        # a===p (mod m) => a**2===p**2 (mod m)
        # 이를 이용해 이진법으로 64개의 리스트를 만들기
        for i in range(64):
            if i == 0:
                mod_dict[i] = mod
            else:
                mod_dict[i] = (mod_dict[i-1])**2 % modulo
        # a===c (mod m), b===d (mod m) => ab===cd (mod m)
        # 이를 이용해 mod_dict에서 이들을 조합해 나머지를 구한다.
        for i in range(64):
            if binary_index[i]:
                final_mod *= mod_dict[i]*binary_index[i]
                final_mod %= modulo
        # base-1의 modulo를 법으로 하는 합동식에서 곱셈의 역원 구하기
        multiply_reverser:int = eea(base - 1, modulo, 1)[0] % modulo
        final_mod = ((final_mod - 1) * (multiply_reverser)) % modulo
        return final_mod

def eea(a:int, b:int, d:int) -> list[int]:
    x_y_seq_memo:list[list[int]] = [[1,0],[0,1]]
    r_memo:list[int] = [a,b]
    q_i:int = 0
    i:int = 2
    while True:
        q_i = r_memo[(i-2)%2] // r_memo[(i-1)%2]
        r_memo[i%2]=r_memo[(i-2)%2] % r_memo[(i-1)%2]
        for j in range(2):
            x_y_seq_memo[i%2][j]=x_y_seq_memo[(i-2)%2][j]-x_y_seq_memo[(i-1)%2][j]*q_i
        if r_memo[i%2]==d:
            break
        else:
            i += 1
    return x_y_seq_memo[i%2]

a, b = list(map(int, input().split(" ")))
prime_factor = factorize(a)
mod = 1
modulo = 1000000007
for i in prime_factor:
    mod *= prime_power_divisor_sum(i, prime_factor[i]*b,modulo)
    mod %= modulo
print(mod)