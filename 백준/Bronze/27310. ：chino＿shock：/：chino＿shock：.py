# A번 - :chino_shock:

emoji_list = list(input())
input_level = sum([i == "_" for i in emoji_list])*5 + sum([i == ":" for i in emoji_list]) + len(emoji_list)
print(input_level)