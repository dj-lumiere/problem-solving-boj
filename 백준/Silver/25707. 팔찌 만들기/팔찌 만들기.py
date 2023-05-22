# 25707 팔찌 만들기

N = int(input())
bracelet = sorted([int(i) for i in input().split(" ")])


def bracelet_length(bracelet: list[int]) -> int:
    result = 0
    for index, value in enumerate(bracelet):
        result += abs(bracelet[index - 1] - value)
    return result


print(bracelet_length(bracelet))