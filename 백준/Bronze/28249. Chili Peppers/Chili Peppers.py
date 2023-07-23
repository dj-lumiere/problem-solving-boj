# 28249 Chili Peppers

spiciness = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000,
}
T = int(input())
total_spiciness = 0
for _ in range(T):
    chili_name = input()
    total_spiciness += spiciness[chili_name]
print(total_spiciness)