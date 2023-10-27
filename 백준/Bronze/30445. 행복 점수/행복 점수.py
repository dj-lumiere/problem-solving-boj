# 30445 행복 점수

sentence = input()
happy_point = sum([letter in "HAPPY" for letter in sentence])
sad_point = sum([letter in "SAD" for letter in sentence])
print(
    f"{(happy_point) / (happy_point + sad_point) * 100 if any((happy_point, sad_point)) else 50:.2f}"
)