# 1463 1로 만들기
from sys import setrecursionlimit
setrecursionlimit(100000000)
def sol():
    N = int(input())
    oneify_dict = {1:0,2:1,3:1}

    def oneify(N) -> int:
        if N in oneify_dict:
            return oneify_dict[N]
        else:
            return (min(N%2+1+oneify(N//2),N%3+1+oneify(N//3)))

    print(oneify(N))

sol()