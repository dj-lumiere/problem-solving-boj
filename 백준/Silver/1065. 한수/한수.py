# 1065 한수

is_hansu = [False] * 1001
for i in range(1001):
    if len(str(i)) <= 2:
        is_hansu[i] = True
    elif len(str(i)) == 3 and int(str(i)[1])*2==int(str(i)[0])+int(str(i)[2]):
        is_hansu[i] = True
is_hansu[0] = False
N = int(input())
print(sum(is_hansu[:N+1]))