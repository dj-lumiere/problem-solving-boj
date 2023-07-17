N = int(input())
print("Gnomes:")
for _ in range(N):
    gnome1, gnome2, gnome3 = map(int, input().split(" "))
    if gnome1 > gnome2 > gnome3 or gnome1 < gnome2 < gnome3:
        print("Ordered")
    else:
        print("Unordered")