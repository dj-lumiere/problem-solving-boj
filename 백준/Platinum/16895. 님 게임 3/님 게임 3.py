# 16895 님 게임 3

answer: int = 0


def xor(a: list[int]) -> int:
    answer = 0
    for i in a:
        answer ^= i
    return answer


N: int = int(input())
P: list[int] = [int(i) for i in input().split(" ")]
all_xor: int = xor(P)
if all_xor:
    for value in P:
        if value >= value ^ all_xor:
            answer += 1
else:
    answer = 0
print(answer)
