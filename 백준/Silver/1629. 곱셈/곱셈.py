def exp_big(base: int, index: int, modulo: int):
    mod_list = dict()
    mod = base % modulo
    binary_index = [index//(2**i)%2 for i in range(32)]
    final_mod = 1
    for i in range(32):
        if i == 0:
            mod_list[i] = mod
        else:
            mod_list[i] = (mod_list[i-1])**2 % modulo
    for i in range(32):
        if binary_index[i]:
            final_mod *= mod_list[i]*binary_index[i]
            final_mod %= modulo
    return final_mod 

a, b, c = list(map(int, input().split(" ")))
print(exp_big(a, b, c))