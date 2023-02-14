n = int(input())
a_list = list(map(int, input().split()))
x = int(input())

def two_sum_pairs(number_list:list[int], target_number: int) -> int:
    number_dict = dict()
    pair_count = 0
    for i, number in enumerate(number_list):
        number_dict[number] = i
    for i in range(1, (target_number - 1)//2+1):
        if target_number - i in number_dict and i in number_dict:
            pair_count += 1
    return pair_count

print(two_sum_pairs(a_list, x))