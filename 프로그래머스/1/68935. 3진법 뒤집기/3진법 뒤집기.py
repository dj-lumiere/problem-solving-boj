import math
def solution(n):
    digit = int(math.log(n, 3)) + 1
    answer = 0
    base3_digit_list = [0 for col in range(digit)]
    for i in range(digit):
        base3_digit_list[i] = n % 3
        n = (n - (n % 3)) // 3
        answer = answer + (base3_digit_list[i] * (3 ** (digit - i - 1)))
    return answer