# 30017 치즈버거 만들기

patty_count, cheese_count = map(int, input().split(" "))
pair_count = min(patty_count - 1, cheese_count)
print(2 * pair_count + 1)