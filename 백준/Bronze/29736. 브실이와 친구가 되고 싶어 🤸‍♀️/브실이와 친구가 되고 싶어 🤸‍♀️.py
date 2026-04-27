# 29736 브실이와 친구가 되고 싶어 🤸‍♀️

has_friend = [False] * 10001
A, B = map(int, input().split(" "))
has_friend[A : B + 1] = [True] * (B - A + 1)
K, X = map(int, input().split(" "))
can_be_friend = sum(has_friend[max(K - X, 0) : K + X + 1])
if not can_be_friend:
    print("IMPOSSIBLE")
else:
    print(can_be_friend)