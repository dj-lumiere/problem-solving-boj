# 30445 행복 점수

sentence = input()
happy_point = sum([letter in "HAPPY" for letter in sentence])
sad_point = sum([letter in "SAD" for letter in sentence])
happiness = (
    (happy_point) * 100000 // (happy_point + sad_point)
    if any((happy_point, sad_point))
    else 50000
)
int_part, frac_part = divmod(happiness, 1000)
frac_part, rounding_part = divmod(frac_part, 10)
if rounding_part >= 5:
    frac_part += 1
    if frac_part >= 100:
        frac_part -= 100
        int_part += 1
print(f"{int_part}.{frac_part:0>2}")