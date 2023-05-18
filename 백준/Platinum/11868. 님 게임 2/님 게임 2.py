# 11868 님 게임 2


def xor(a: list[int]) -> int:
    answer = 0
    for i in a:
        answer ^= i
    return answer


N = int(input())
P = list(map(int, input().split(" ")))

if xor(P):
    print("koosaga")
else:
    print("cubelover")
