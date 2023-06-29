# 23235 The Fastest Sorting Algorithm In The World

i = 0
MAX_ITER = 100
while i < MAX_ITER:
    i += 1
    sorting_list = list(map(int, input().split(" ")))
    if sorting_list == [0]:
        break
    print(f"Case {i}: Sorting... done!")