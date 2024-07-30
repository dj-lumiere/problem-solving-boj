def solution(x):
    digit_sum = 0
    x_str = str(x)
    x_len = len(x_str)
    for i in range(x_len):
        digit_sum = digit_sum + int(x_str[i])
    if x % digit_sum == 0:
        return True
    else:
        return False