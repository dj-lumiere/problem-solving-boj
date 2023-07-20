# 5300 Fill the Rowboats!

N = int(input())
counting = []
for i in range(1, N+1):
    counting.append(str(i))
    if i % 6 == 0:
        counting.append("Go!")
if counting[-1] != "Go!":
    counting.append("Go!")
print(*counting)