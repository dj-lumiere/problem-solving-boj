# 16495 열 순서

alphabet_to_number = lambda x: ord(x) - ord("A")

column_alphabet_list = list(map(alphabet_to_number, list(input())))[::-1]
digits = len(column_alphabet_list)
print(
    sum([j * (26**i) for i, j in enumerate(column_alphabet_list)])
    + (26**digits - 26) // 25
    + 1
)