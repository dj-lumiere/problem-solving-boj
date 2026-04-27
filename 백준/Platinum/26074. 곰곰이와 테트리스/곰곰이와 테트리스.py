# 26074 곰곰이와 테트리스

N, M = map(int, input().split())
P = list(map(int, input().split()))

if (N, M) in [(1,2),(2,1)]:
    print("ChongChong")
else:
    print("GomGom")