# 28702 FizzBuzz

int_position, int_value = -1, -1
result = 0
for i in range(3):
    word = input()
    if word in ["FizzBuzz", "Fizz", "Buzz"]:
        continue
    int_position, int_value = i, int(word)
result = (3 - int_position) + int_value
if result % 15 == 0:
    print("FizzBuzz")
elif result % 5 == 0:
    print("Buzz")
elif result % 3 == 0:
    print("Fizz")
else:
    print(result)