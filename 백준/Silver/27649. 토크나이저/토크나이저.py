# 27649 토크나이저

from re import split

tokens = split(r'(<|>|\|\||&&|\(|\)|\s)',input())
print_tokens = [i for i in tokens if i != " " and i != ""]
print(*print_tokens)