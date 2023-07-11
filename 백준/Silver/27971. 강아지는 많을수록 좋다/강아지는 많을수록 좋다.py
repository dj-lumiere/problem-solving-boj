# 27971 강아지는 많을수록 좋다

MAX_MOVEMENT = 9999999999999
INVALID = -99999999999999
N, M, A, B = map(int, input().split(" "))
how_many_movement = [MAX_MOVEMENT for _ in range(N + 1)]
for _ in range(M):
    L, R = map(int, input().split(" "))
    how_many_movement[L : R + 1] = [INVALID] * (R - L + 1)
# print(N, M, A, B)
# print(how_many_movement)
how_many_movement[0] = 0
how_many_movement[A] = min(how_many_movement[A], 1)
how_many_movement[B] = min(how_many_movement[B], 1)

for i, v in enumerate(how_many_movement):
    if v == INVALID:
        continue
    compare_list_sub = []
    if i - A >= 0 and how_many_movement[i - A] != INVALID:
        compare_list_sub.append(i - A)
    if i - B >= 0 and how_many_movement[i - B] != INVALID:
        compare_list_sub.append(i - B)
    if not compare_list_sub:
        continue
    how_many_movement[i] = min(
        MAX_MOVEMENT, *[how_many_movement[i] + 1 for i in compare_list_sub]
    )
# print(how_many_movement)
if how_many_movement[-1] == MAX_MOVEMENT:
    print(-1)
else:
    print(how_many_movement[-1])