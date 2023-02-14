from math import log10

num_list = []

roman_convert_dict = dict({"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000})
number_convert_dict = dict({1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"})

for i in range(2):
    num_list.append(input())

def roman_number(roman:str) -> int:
    number_list = []
    for i in range(len(roman)):
        number_list.append(roman_convert_dict[roman[i]])
    for i in range(len(roman)-1):
        if number_list[i] * 5 == number_list[i+1] or number_list[i] * 10 == number_list[i+1]:
            number_list[i] *= -1
    return sum(number_list)

num_list = [roman_number(i) for i in num_list]

def number_roman(number:int) -> str:
    digits = int(log10(number))+1
    roman_string = ""
    for i in range(digits, 0, -1):
        ith_digit = (number // (10 ** (i-1))) % 10
        ith_digit_value = 10 ** (i-1)
        if ith_digit == 9:
            roman_string += number_convert_dict[ith_digit_value]+number_convert_dict[ith_digit_value*10]
        elif 5 <= ith_digit and ith_digit < 9:
            roman_string += number_convert_dict[ith_digit_value*5]+ (ith_digit-5)*number_convert_dict[ith_digit_value]
        elif ith_digit == 4:
            roman_string += number_convert_dict[ith_digit_value]+number_convert_dict[ith_digit_value*5]
        else:
            roman_string += ith_digit*number_convert_dict[ith_digit_value]
    return roman_string

print(sum(num_list))
print(number_roman(sum(num_list)))