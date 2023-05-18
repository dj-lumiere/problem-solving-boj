# 2877 4와 7

from math import log2, floor

K = int(input())
digit = floor(log2(K + 1))
Kth_digit_in_binary = list(bin(K - 1 - (2**digit - 2)))[2:]
Kth_digit_in_binary = ["0"]*(digit - len(Kth_digit_in_binary)) + Kth_digit_in_binary
print("".join(["4" if i == "0" else "7" for i in Kth_digit_in_binary]))