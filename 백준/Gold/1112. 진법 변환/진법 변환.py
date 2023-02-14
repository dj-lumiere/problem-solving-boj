# 1112 진법 변환

x, b = list(map(int, input().split(" ")))

def nega_n_ary_change(num, n) -> str:
    nega_n_ary_list: list[int] = []
    quotient, mod = num, 0
    while quotient:
        quotient, mod = divmod(quotient, n)
        if mod:
            quotient += 1
            mod -= n
        nega_n_ary_list.append(mod)
    return "".join(map(str, nega_n_ary_list[::-1]))


def n_ary_change(num, n) -> str:
    n_ary_list: list[int] = []
    quotient, mod = num, 0
    while quotient:
        quotient, mod = divmod(quotient, n)
        n_ary_list.append(mod)
    return "".join(map(str, n_ary_list[::-1]))


if b > 0 and x < 0:
    print("-" + n_ary_change(-1*x, b))
elif b > 0 and x > 0:
    print(n_ary_change(x, b))
elif x == 0:
    print("0")
else:
    print(nega_n_ary_change(x, b))
