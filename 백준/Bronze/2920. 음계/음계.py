# 2920 음계

note_list = list(map(int, input().split()))

if note_list == [i for i in range(1, 8 + 1)]:
    print("ascending")
elif note_list == [i for i in range(8, 1 - 1, -1)]:
    print("descending")
else:
    print("mixed")