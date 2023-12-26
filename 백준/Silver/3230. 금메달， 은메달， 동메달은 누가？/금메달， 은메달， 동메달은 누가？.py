# 3230 금메달, 은메달, 동메달은 누가?

N, M = map(int, input().split(" "))
rank = []
for i in range(1, N + 1):
    current_rank = int(input())
    rank.insert(current_rank - 1, i)
rank = (rank[:M])[::-1]
final_rank = []
for i in rank:
    current_rank = int(input())
    final_rank.insert(current_rank - 1, i)
final_rank = final_rank[:3]
print(*final_rank, sep="\n")