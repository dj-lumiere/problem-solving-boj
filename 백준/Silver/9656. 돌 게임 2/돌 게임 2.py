states = [set() for i in range(1001)]
nimber = [0 for _ in range(1001)]
for i in range(1, 1001):
    if i >= 1:
        states[i].add(i - 1)
    if i >= 3:
        states[i].add(i - 3)

for i, v in enumerate(states):
    possible_nimbers = sorted([nimber[s] for s in v])
    for j in range(2001):
        if j not in possible_nimbers:
            nimber[i] = j
            break

n = int(input())
print("SK" if nimber[n] == 0 else "CY")
