# C번 - 등차수열의 합

from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def solution():
    # 일단 등차인지 아닌지 체크
    N = int(input())
    A = [int(i) for i in input().strip().split(" ")]
    if N == 1:
        return f"YES\n{A[0]*2}\n{A[0]*-1}"
    difference = A[1] - A[0]
    for index, value in enumerate(A):
        if index == 0:
            continue
        elif value - A[index - 1] != difference:
            return "NO"
    # 등차면 한 줄에는 2배, 한 줄에는 -1배
    return (
        "YES"
        + "\n"
        + (" ".join([str(i * 2) for i in A]))
        + "\n"
        + (" ".join([str(-i) for i in A]))
    )


print(solution())
