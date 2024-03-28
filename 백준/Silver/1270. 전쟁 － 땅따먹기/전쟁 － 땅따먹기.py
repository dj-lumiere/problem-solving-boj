from collections import Counter, defaultdict

n = int(input())
for i in range(n):
    a, *b = map(int, input().split())
    b_count = Counter(b)
    frequency_count = defaultdict(list)
    for key, value in b_count.items():
        frequency_count[value].append(key)
    max_freq = max(frequency_count.keys())
    if max_freq * 2 <= a:
        print("SYJKGW")
    elif len(frequency_count[max_freq]) >= 2:
        print("SYJKGW")
    else:
        print(*frequency_count[max_freq])