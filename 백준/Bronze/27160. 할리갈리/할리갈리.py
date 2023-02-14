def hally_gally():
    fruit_list = ["STRAWBERRY", "BANANA", "LIME", "PLUM"]
    fruit_dict = {i:0 for i in fruit_list}

    N = int(input())

    for i in range(N):
        fruit, count = list(map(str, input().split(" ")))
        fruit_dict[fruit] += int(count)

    for i, j in fruit_dict.items():
        if j == 5:
            print("YES")
            return
    print("NO")
    return
hally_gally()