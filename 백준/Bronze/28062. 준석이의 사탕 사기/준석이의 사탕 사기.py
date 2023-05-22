# B번 - 준석이의 사탕 사기

N = int(input())
A = [int(i) for i in input().split(" ")]
INT_MAX = 1002
is_odd = lambda x: not not x % 2
filter_odd = lambda x: x if x % 2 else INT_MAX
odd_list = [filter_odd(i) for i in A]
odd_count = sum([is_odd(i) for i in A])
odd_min = min(odd_list)
all_candy_count = sum(A)
if odd_count % 2:
    print(all_candy_count - odd_min)
else:
    print(all_candy_count)