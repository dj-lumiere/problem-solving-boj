# 9934 완전 이진 트리

K = int(input())
K -= 1
A = list(map(int, input().split(" ")))
levels = [[] for i in range(K + 1)]

def height_traverse(level: int, offset: int):
    if level == 0:
        levels[level].append(A[offset])
        return
    else:
        levels[level].append(A[offset])
        height_traverse(level-1, offset - 2**(level-1))
        height_traverse(level-1, offset + 2**(level-1))
height_traverse(K, 2**K - 1)
levels.reverse()
for i in range(K + 1):
    print(*levels[i], sep=' ')