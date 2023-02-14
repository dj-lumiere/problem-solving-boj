from math import log10

def d(n: int):
    d_n = n
    digit = int(log10(n))+1
    for i in range(digit):
        d_n += (n // (10 ** i)) % 10
    return d_n

num_list: list[bool] = [False] + [True for i in range(10000)]
for i, j in enumerate(num_list):
    if j:
        next_int = i
        while True:
            next_int = d(next_int)
            if next_int <= 10000:
                num_list[next_int] = False
            else:
                break
for i, j in enumerate(num_list):
    if j:
        print(i)