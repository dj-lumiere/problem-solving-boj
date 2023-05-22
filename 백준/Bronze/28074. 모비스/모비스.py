# 28074 모비스

target_list = list(input())
compare_list = list("MOBIS")
print("YES" if all([i in target_list for i in compare_list]) else "NO")