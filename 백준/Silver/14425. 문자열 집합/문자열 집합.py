from sys import stdin

element_count, query_count = list(map(int, input().split(" ")))
set_dict:dict[str, int] = dict()
hit_count:int = 0
for i in range(element_count):
    element:str = stdin.readline().rstrip()
    set_dict[element] = i
for i in range(query_count):
    query:str = stdin.readline().rstrip()
    if query in set_dict:
        hit_count += 1

print(hit_count)