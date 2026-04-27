n = int(input())
a = list(map(int, input().split()))
one_count = a.count(1)
two_count = a.count(2)
three_count = a.count(3)
if one_count == n + 1 and two_count == n - 1:
    print("2\n1")
elif one_count == n + 1 and three_count == n - 1:
    print("3\n1")
elif two_count == n + 1 and one_count == n - 1:
    print("1\n2")
elif two_count == n + 1 and three_count == n - 1:
    print("3\n2")
elif three_count == n + 1 and one_count == n - 1:
    print("1\n3")
elif three_count == n + 1 and two_count == n - 1:
    print("2\n3")