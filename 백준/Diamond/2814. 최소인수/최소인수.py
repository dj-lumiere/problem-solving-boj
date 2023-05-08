# 2814 최소인수

N, P = map(int, input().split(" "))


# a까지의 소수를 찾기
def find_prime(a: int) -> list[int]:
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
        prime_list2 = [i for (i, j) in enumerate(prime_list) if j]
        return prime_list2


def p_as_minimum_prime_factor_count(
    limit: int,
    remaining_choices: int,
    current_factor: int,
    current_position: int,
    prime_list: list[int],
) -> int:
    answer: int = 0
    for index, value in enumerate(prime_list):
        if index >= current_position:
            if remaining_choices > 1:
                next_factor = current_factor * value
                if next_factor <= limit:
                    answer_sub = p_as_minimum_prime_factor_count(
                        limit,
                        remaining_choices - 1,
                        next_factor,
                        index + 1,
                        prime_list,
                    )
                    # 인수가 limit을 초과하면 break
                    if answer_sub == 0:
                        break
                    answer += answer_sub
                # 인수가 limit을 초과하면 break
                else:
                    break
            else:
                next_factor = current_factor * value
                if next_factor <= limit:
                    answer_sub = limit // next_factor
                    answer += answer_sub
                else:
                    break
    return answer


if N >= 2 and P * P > 10**9:
    print(0)
elif N == 2 and P * P <= 10**9:
    print(P * P)
elif N == 1:
    print(P)
else:
    start = 0
    end = 10**9 + 1
    prime_list = find_prime(P - 1)
    final_answer = 0
    while start + 1 < end:
        mid = (start + end) // 2
        answer = mid // P
        # 2*3*5*7*11*13*17*19*23*29 > 10**9
        for i in range(1, 10):
            sign = -1 if i % 2 else 1
            answer += sign * p_as_minimum_prime_factor_count(
                limit=mid,
                remaining_choices=i,
                current_factor=P,
                current_position=0,
                prime_list=prime_list,
            )
        if answer < N:
            start = mid
        elif answer > N:
            end = mid
        else:
            # 이분탐색을 하다보면 값이 P의 배수가 아니게 될 수도 있는데 그걸 걸러줌
            minimum_factor_P_check = True
            if mid % P == 0:
                # P 미만의 모든 인수로 다 나눠봄
                for prime in prime_list:
                    if not mid % prime:
                        minimum_factor_P_check = False
            else:
                minimum_factor_P_check = False
            # 정답임
            if minimum_factor_P_check:
                final_answer = mid
                break
            # 정답이 아닐 경우 다시 탐색
            else:
                end = mid
    print(final_answer)
