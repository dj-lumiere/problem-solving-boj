# 28419 더하기

# 홀수 자리의 합 - 짝수 자리의 합을 a라 하면
# 홀수 자리에서 +1을 하면 a+1
# 짝수 자리에서 +1을 하면 a-1
# 3일 때 주의 -> a>0이면 복구 불가능


def get_difference(A: list[int]) -> int:
    odd_digit_sum = 0
    even_digit_sum = 0
    for i, v in enumerate(A, start=1):
        if i & 1:
            odd_digit_sum += v
        else:
            even_digit_sum += v
    return odd_digit_sum - even_digit_sum


N = int(input())
A = list(map(int, input().split(" ")))
difference = get_difference(A)
if N == 3 and difference > 0:
    print("-1")
else:
    print(abs(difference))