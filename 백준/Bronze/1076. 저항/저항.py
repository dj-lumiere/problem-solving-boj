# 1076 저항

resistor_info = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}
answer = 0
for i in range(3):
    color = input()
    if i == 0:
        answer += resistor_info[color]
    if i == 1:
        answer *= 10
        answer += resistor_info[color]
    if i == 2:
        answer *= 10 ** resistor_info[color]
print(answer)