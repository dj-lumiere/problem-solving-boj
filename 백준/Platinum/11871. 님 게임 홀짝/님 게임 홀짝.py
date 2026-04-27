# 11871 님 게임 홀짝


def xor(a: list[int]) -> int:
    answer = 0
    for i in a:
        answer ^= i
    return answer


def nimberify(x):
    if x&1:return (x+1)//2
    return x//2-1

N = int(input())
P = list(map(int, input().split(" ")))
P = list(map(nimberify, P))

if xor(P):
    print("koosaga")
else:
    print("cubelover")
