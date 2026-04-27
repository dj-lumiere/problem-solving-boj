from collections import Counter

n = int(input())
a = list(map(int, input().split()))
a_count = Counter(a)
if 0 not in a_count:
    a_count[0]=0
if 1 not in a_count:
    a_count[1]=0
zero_count = a_count[0]
one_count = a_count[1]
others_count = n-zero_count-one_count
answer = (zero_count**2-zero_count)//2+zero_count*one_count*2+zero_count*others_count*1
print(answer)