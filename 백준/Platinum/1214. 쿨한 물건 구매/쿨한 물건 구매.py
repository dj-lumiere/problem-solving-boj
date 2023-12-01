# 1214 쿨한 물건 구매


def solution(D, P, Q):
    if D % P == 0 or D % Q == 0:
        return D
    P, Q = max(P, Q), min(P, Q)
    max_P = (D + P - 1) // P 
    answer = P * max_P
    for i in range(max_P - 1, -1, -1): # P원짜리를 i개 쓴 경우 생각
        q_quantity, remainder = divmod(D - i * P, Q)
        if remainder == 0:
            return D
        q_quantity += 1
        minimum_value = i * P + q_quantity * Q
        if answer == minimum_value:
            break
        answer = min(answer, minimum_value)
    return answer


D, P, Q = map(int, input().split(" "))
print(solution(D, P, Q))