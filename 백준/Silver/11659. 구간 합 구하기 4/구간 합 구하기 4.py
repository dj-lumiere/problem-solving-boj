from sys import stdin, stdout

def partial_sum_list(num_list: list[int]):
    num_list_modify = [0]
    for i, num in enumerate(num_list):
        num_list_modify.append(num_list_modify[i] + num)
    return num_list_modify

def partial_sum(num_list:list[int], start:int, end:int) -> int:
    return num_list[end]-num_list[start-1]

def make_number_list() -> list[int]:
    return list(map(int, input().split(" ")))

N, M = list(map(int, input().split(" ")))
number_list = make_number_list()
number_list = partial_sum_list(number_list)
for h in range(M):
    i, j = list(map(int, stdin.readline().rstrip().split(" ")))
    stdout.writelines(f"{partial_sum(number_list, i, j)}\n")