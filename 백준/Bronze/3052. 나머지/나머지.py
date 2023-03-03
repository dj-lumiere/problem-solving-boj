# 3052 나머지

mod_42 = lambda x: x % 42
mod_list = set(map(mod_42, [int(input()) for _ in range(10)]))
print(len(mod_list))