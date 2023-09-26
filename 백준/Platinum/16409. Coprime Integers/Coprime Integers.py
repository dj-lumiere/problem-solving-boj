def calculate_mobius_function(limit):
    result = [1] * (limit + 1)
    check = [False] * (limit + 1)
    result[1] = 1
    check[1] = True
    for i in range(2, limit + 1):
        if check[i]:
            continue
        j = 1
        while i * j <= limit:
            check[i * j] = True
            result[i * j] = (result[i * j] * -1) if j % i else 0
            j += 1
    return result


mobius_function = calculate_mobius_function(10**7)
result = 0
a, b, c, d = map(int, input().split(" "))
for i in range(1, min(b, d) + 1):
    result += mobius_function[i] * (b // i - (a - 1) // i) * (d // i - (c - 1) // i)
print(result)