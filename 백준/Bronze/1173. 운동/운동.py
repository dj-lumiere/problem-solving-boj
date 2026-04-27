import os

tokens = iter(os.read(0, os.fstat(0).st_size).split())
N, m, M, T, R = map(int, tokens)
if m + T > M:
    print(-1)
else:
    x = m
    exercise_time = 0
    rest_time = 0
    while exercise_time < N:
        if x + T > M:
            rest_time += 1
            x = max(x-R, m)
            continue
        x += T
        exercise_time += 1
    print(rest_time+exercise_time)
