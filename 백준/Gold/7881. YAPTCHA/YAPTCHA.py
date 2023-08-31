# 7881 YAPTCHA

from sys import stdin, stdout

# stdin = open("test_input.txt", "r")
# stdout = open("test_output.txt", "w")

# Wilson's theorem에 의해, 3k+7의 소수성만 판별하면 됨.


# a까지의 소수를 찾기
def find_prime(a: int) -> list[bool]:
    if a == 1:
        return []
    else:
        finder_limit = a
        prime_list: list[bool] = [True for i in range(0, finder_limit + 1)]
        prime_list[0] = False
        prime_list[1] = False
        for x in range(1, int(finder_limit**0.5) + 1):
            if prime_list[x]:
                prime_list[x : finder_limit + 1 : x] = [False] * (finder_limit // x)
                prime_list[x] = True
            else:
                continue
        return prime_list


prime_list = find_prime(10**6 * 3 + 7)
answer_accumulated_sum = [0] * (10**6 + 1)
for i in range(1, 10**6 + 1):
    if prime_list[3 * i + 7]:
        answer_accumulated_sum[i] = answer_accumulated_sum[i - 1] + 1
    else:
        answer_accumulated_sum[i] = answer_accumulated_sum[i - 1]

test_cases = int(stdin.readline().strip())
for _ in range(test_cases):
    target = int(stdin.readline().strip())
    stdout.write(f"{answer_accumulated_sum[target]}\n")