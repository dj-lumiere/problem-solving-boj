# 10827 a^b

a, b = list(map(str, input().split(" ")))
a_int, a_frac = list(map(str, a.split(".")))

dec_pt_pos = len(a_frac) * int(b)


a2 = str(a_int + a_frac).lstrip("0")


def big_multiply(a: str, b: str):
    if len(a) < len(b):
        a, b = b, a
    total_length = len(a) + len(b)
    a_list = list(map(int, list(a)[::-1]))
    b_list = list(map(int, list(b)[::-1]))
    multiply_list = [0] * total_length
    for i in range(total_length - 1):
        digit_sub = sum(a_list[j] * b_list[i - j] for j in range(max(0, i - len(b) + 1), min(len(a), i + 1)))
        multiply_list[i] += digit_sub
        multiply_list[i + 1], multiply_list[i] = divmod(multiply_list[i], 10)
    return "".join(map(str, multiply_list[::-1])).lstrip("0")


power_list = [a2]
for i in range(1, 6+1):
    power_list.append(big_multiply(power_list[-1], power_list[-1]))

b_bin = list(map(int, (bin(int(b))[2:])[::-1]))
powered_num = "1"

for i, j in enumerate(b_bin):
    if j:
        powered_num = big_multiply(powered_num, power_list[i])

if len(powered_num) <= dec_pt_pos:
    powered_num_int, powered_num_frac = (
        "0",
        "0" * (dec_pt_pos - len(powered_num)) + powered_num,
    )
else:
    powered_num_int, powered_num_frac = (
        powered_num[: -1 * dec_pt_pos],
        powered_num[-1 * dec_pt_pos :],
    )

print(powered_num_int + "." + powered_num_frac)