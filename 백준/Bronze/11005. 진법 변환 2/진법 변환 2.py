# 11005 진법 변환 2


def n_ary_change(number: str, original_base: int, converting_base: int) -> str:
    number_in_base_10 = int(number, base=original_base)
    result = []
    while number_in_base_10 > 0:
        number_in_base_10, mod = divmod(number_in_base_10, converting_base)
        result.append(mod)
    for i, v in enumerate(result):
        if v >= 10:
            result[i] = chr(ord("A") + v - 10)
        else:
            result[i] = str(v)
    result.reverse()
    return "".join(result)


N, B = input().split(" ")
print(n_ary_change(N, 10, int(B)))