# 26597 이 사람 왜 이렇게 1122를 좋아함?

from sys import stdin

N = int(input())
def up_down(N):
    upper_limit, lower_limit = [-1*10**18, 10**18]
    gotit_time = 0
    paradox_time = 0
    for i in range(1, N+1):
        # interval 조건에 따라서 x_interval 수정
        number, command = list(map(str, stdin.readline().rstrip().split(" ")))
        number = int(number)
        if paradox_time == 0:
            # x^ 이면 상한을 x+1로 조정
            if command == "^":
                upper_limit = max(upper_limit,number + 1)
            # xv 이면 하한을 x-1로 조정
            elif command == "v":
                lower_limit = min(lower_limit,number - 1)

        # interval 조건과 모순될 때
        # 1) x^이 주어졌는데 하한이 x 미만인 경우
        # 2) xv가 주어졌는데 상한이 x 이상인 경우
        # 모순될 경우 Paradox + 명령 횟수 출력
        if lower_limit < upper_limit and paradox_time == 0:
            paradox_time = i
        # 하한-상한이 0인 경우 I got it! + 명령 횟수 출력
        if upper_limit == lower_limit and gotit_time == 0:
            gotit_time = i

    if upper_limit > lower_limit:
        print("Paradox!")
        print(paradox_time)
    elif upper_limit == lower_limit:
        print("I got it!")
        print(gotit_time)
    # 하한 - 상한이 0이 아닌 경우 Hmm... 출력
    elif upper_limit < lower_limit:
        print("Hmm...")


up_down(N)