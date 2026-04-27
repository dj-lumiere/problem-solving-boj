# 21921 블로그

N, X = map(int, input().split())
visitor_list = list(map(int, input().split()))
visitor_sub = 0
max_visitor_sub = 0
max_visitor_freq = 0
for i, v in enumerate(visitor_list):
    if i >= N:
        break
    visitor_sub += v - (visitor_list[i - X] if i - X >= 0 else 0)
    if visitor_sub > max_visitor_sub:
        max_visitor_sub = visitor_sub
        max_visitor_freq = 1
    elif visitor_sub == max_visitor_sub:
        max_visitor_freq += 1
print(f"{max_visitor_sub}\n{max_visitor_freq}" if max_visitor_sub else "SAD")