from bisect import bisect_left, bisect_right

n, m = map(int, input().split(" "))
mention_count = list(map(int, input().split(" ")))
mention_count.sort()
multiple_ping_person = n - bisect_left(mention_count, 2)
required_messages = sum(mention_count[-multiple_ping_person:]) // multiple_ping_person if multiple_ping_person else 0
ping_person_cutoff = bisect_right(mention_count, required_messages)
if required_messages > m:
    print(-1)
else:
    result = [
        max(0, ping_person_cutoff - bisect_left(mention_count, i + 1)) for i in range(m)
    ]
    result[0] = n
    print(*result)
