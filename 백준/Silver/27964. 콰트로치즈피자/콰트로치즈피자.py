# 27964 콰트로치즈피자

N = int(input())
unique_cheese = set()
topping_list = input().split(" ")
for topping in topping_list:
    if topping[-6:] == "Cheese":
        unique_cheese.add(topping)
if len(unique_cheese) >= 4:
    print("yummy")
else:
    print("sad")
