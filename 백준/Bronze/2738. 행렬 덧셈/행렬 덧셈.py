# 2738 행렬 덧셈

N, M = list(map(int, input().split(" ")))
a_list = [list(map(int, input().split(" "))) for i in range(N)]
b_list = [list(map(int, input().split(" "))) for i in range(N)]
sum_list = [[a_list[y][x] + b_list[y][x] for x in range(M)] for y in range(N)]
print("\n".join(" ".join(map(str, i)) for i in sum_list))