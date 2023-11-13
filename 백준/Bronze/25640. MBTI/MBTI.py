# 25640 MBTI

T = input()
N = int(input())
friend_type = [input() for _ in range(N)]
print(sum(i == T for i in friend_type))