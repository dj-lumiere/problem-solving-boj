number_list = []
number_temp = 0
number_pos = 0
while True:
    try:
        n = int(input())
        number_list.append(n)
    except:
        break
for i, number in enumerate(number_list):
    if number_temp < number:
        number_temp, number_pos = number, i
print(f"{number_temp}\n{number_pos+1}")