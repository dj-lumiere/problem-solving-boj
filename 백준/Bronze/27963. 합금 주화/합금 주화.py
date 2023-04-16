d1, d2, chi = map(int, input().split(" "))
mass = 100
volume = chi / max(d1, d2) + (100 - chi) / min(d1, d2)
print(mass / volume)
