# 27962 오렌지먹은지오랜지

N = int(input())
target_string = input()
counter = 0
string_from_left = []
string_from_right = []
while True:
    if counter >= N:
        print("NO")
        break
    else:
        string_from_left = string_from_left + [target_string[counter]]
        string_from_right = [target_string[-counter - 1]] + string_from_right
        if sum([i!=j for (i, j) in zip(string_from_left, string_from_right)]) == 1:
            print("YES")
            break
        else:
            counter += 1
