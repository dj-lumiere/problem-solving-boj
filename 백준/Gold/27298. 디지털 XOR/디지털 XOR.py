# 27298 디지털 XOR

three_number_dict = {
    1: (1, 1, 1),
    2: (2, 2, 2),
    3: (3, 3, 3),
    4: (4, 4, 4),
    5: (5, 5, 5),
    6: (6, 6, 6),
    7: (7, 7, 7),
    8: (5, 6, 9),
    9: (5, 6, 8),
}

four_number_dict = {
    1: (2, 3, 5, 8),
    2: (1, 3, 5, 8),
    3: (1, 2, 5, 8),
    5: (1, 2, 3, 8),
    6: (1, 2, 3, 9),
    8: (1, 2, 3, 5),
    9: (1, 2, 3, 6),
}


def product(target_list: list[int]) -> int:
    result: int = 1
    for x in target_list:
        result = result * x
    return result


N = list(map(int, list(input())))
if (4 in N) or (7 in N):
    number_list: list[int] = [
        sum(
            [
                three_number_dict[i][j] * 10 ** (len(N) - 1 - digit)
                for digit, i in enumerate(N)
            ]
        )
        for j in range(3)
    ]
    print(sum(number_list), 3)
    print(*number_list, sep="\n")
else:
    number_list: list[int] = [
        sum(
            [
                three_number_dict[i][j] * 10 ** (len(N) - 1 - digit)
                for digit, i in enumerate(N)
            ]
        )
        for j in range(3)
    ]
    number_list2: list[int] = [
        sum(
            [
                four_number_dict[i][j] * 10 ** (len(N) - 1 - digit)
                for digit, i in enumerate(N)
            ]
        )
        for j in range(4)
    ]
    if sum(number_list) < sum(number_list2):
        print(sum(number_list), 3)
        print(*number_list, sep="\n")
    elif sum(number_list) > sum(number_list2):
        print(sum(number_list2), 4)
        print(*number_list2, sep="\n")
    else:
        if product(number_list) < product(number_list2):
            print(sum(number_list), 3)
            print(*number_list, sep="\n")
        else:
            print(sum(number_list2), 4)
            print(*number_list2, sep="\n")