# 1292 쉽게 푸는 문제

number_list = [0]

for i in range(1, 60):
    number_list += [i] * i
    if len(number_list) > 1000:
        break
a, b = map(int, input().split(" "))
print(sum(number_list[a : b + 1]))