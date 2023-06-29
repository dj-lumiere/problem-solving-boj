# 27389 Metronome

def my_round_function(numerator: int, denominator: int, digit: int):
    x = numerator * (10 ** (digit + 1)) // denominator
    int_part, frac_part = divmod(x, 10 ** (digit + 1))
    frac_part, rounding_part_check = divmod(frac_part, 10)
    if rounding_part_check >= 5:
        frac_part += 1
    return f"{int_part}.{str(frac_part).zfill(digit)}"

print(my_round_function(int(input()), 4, 2))