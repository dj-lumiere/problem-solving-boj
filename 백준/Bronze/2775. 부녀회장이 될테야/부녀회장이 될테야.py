from sys import stdin

test_case = int(input())

def loading_list_n(n: int) -> list:
    string_list = []
    while n:
        n -= 1
        j = int(stdin.readline().rstrip())
        i = int(stdin.readline().rstrip())
        string_list.append((j, i))
    return string_list

def apt_people_count(floor : int, room : int) -> int:
    a = [[0 for col in range(14)] for row in range(0, 14 + 1)]

    for i in range(14):
        a[0][i] = i + 1
    for i in range(14 + 1):
        a[i][0] = 1

    for j in range(1, 14 + 1):
        for k in range(1, 13 + 1):
            a[j][k] = a[j-1][k] + a[j][k-1]

    print(a[floor][room - 1])

for i in loading_list_n(test_case):
    apt_people_count(i[0], i[1])