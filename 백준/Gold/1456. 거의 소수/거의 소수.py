# 1456 거의 소수
from math import ceil

prime_check_list = [True for i in range(10**7 + 1)]
prime_list = []
prime_check_list[0] = False
prime_check_list[1] = False
for i in range(ceil(10**3.5) + 1):
    if prime_check_list[i]:
        prime_check_list[i::i] = [False] * (ceil(10**7) // i)
        prime_check_list[i] = True
for (i, j) in enumerate(prime_check_list):
    if j:
        prime_list.append(i)
A, B = list(map(int, input().split(" ")))
right_answer = 0
left_answer = 0


def bisect_powered_left(number_list: list[int], target: int, index: int) -> int:
    if number_list[0] ** index > target:
        return 0
    elif number_list[-1] ** index < target:
        return len(number_list)
    else:
        start = 0
        end = len(number_list) - 1
        while start <= end:
            mid = (start + end) // 2
            if number_list[mid] ** index >= target:
                end = mid - 1
            else:
                start = mid + 1
        if number_list[start] ** index == target:
            return start+1
        else:
            return start

i = 1
while True:
    i += 1
    right_answer_increment = bisect_powered_left(prime_list, B, i)
    left_answer_increment = bisect_powered_left(prime_list, A - 1, i)
    if right_answer_increment == left_answer_increment == 0:
        break
    else:
        right_answer += right_answer_increment
        left_answer += left_answer_increment
print(right_answer - left_answer)