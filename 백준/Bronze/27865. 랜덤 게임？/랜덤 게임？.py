from random import randint

n = int(input())
for _ in range(20000):
    x = randint(1, n)
    print(f"? {x}")
    answer = input()
    if answer == "Y":
        print(f"! {x}")
        break