# 2857 FBI

name = [""]
for _ in range(5):
    name.append(input())
fbi_index = [i for i, v in enumerate(name) if "FBI" in v]
if fbi_index:
    print(*fbi_index)
else:
    print("HE GOT AWAY!")
