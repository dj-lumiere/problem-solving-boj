# 1193 분수찾기

x = int(input())
# 분자+분모가 n+1인 아이템의 갯수 n개
# 분자+분모가 2~n+1인 모든 아이템의 갯수를 S(n)이라 하면 S(n)=n(n+1)//2

def sol(x:int) -> str:
    # 분자 분모 선언
    numerator: int = 0
    denominator: int = 0
    # 1. S(n) < x < S(n+1)인 n 찾기
    n: int = 0
    while True:
        if (n+1) ** 2 + (n+1) >= 2 * x and 2 * x >= n**2 + n:
            break
        else:
            n += 1
    x -= (n ** 2 + n)//2 + 1
    n += 1
    # 2. n의 홀짝 여부 확인. n이 홀인 경우 n/1부터 시작, n이 짝인 경우 1/n부터 시작
    if n % 2:
        numerator = n
        denominator = 1
        # 3. x-S(n)번째 아이템 확인
        # (index가 0부터 시작하므로 미리 1을 빼둠)
        numerator -= x
        denominator += x
    else:
        numerator = 1
        denominator = n
        # 3. x-S(n)번째 아이템 확인
        # (index가 0부터 시작하므로 미리 1을 빼둠)
        denominator -= x
        numerator += x
    return f"{numerator}/{denominator}"
print(sol(x))
