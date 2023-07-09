# 1769 3의 배수

digit = list(map(int, list(input().strip())))
operation_count = 0
while len(digit) > 1:
    digit = list(map(int, list(str(sum(digit)))))
    operation_count += 1
print(operation_count)
if digit[0] in [3, 6, 9]:
    print("YES")
else:
    print("NO")
