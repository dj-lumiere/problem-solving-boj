# 27970 OX

# 문자열의 O와 X를 뒤집어서 2진법처럼 처리하면 그게 값이다

a = lambda x: int(x == "O")
string_list = list(map(a, input()))
print(sum([j << i for (i, j) in enumerate(string_list)]) % (10**9 + 7))
