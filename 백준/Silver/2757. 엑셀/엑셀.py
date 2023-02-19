# 2757 엑셀

from math import log, floor

number_to_alphabet = lambda x: chr(x + ord("A"))

while True:
    r, c = list(map(int, input()[1:].split("C")))
    if r == 0 and c == 0:
        break
    else:
        digit = floor(log(c * 25 + 25, 26))
        column_number_for_alphabet = c - (26**digit - 26) // 25 - 1
        column_number_list = [
            column_number_for_alphabet // (26**i) % 26 for i in range(digit)
        ]
        print("".join(map(number_to_alphabet, column_number_list[::-1])), r, sep="")