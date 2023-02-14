from sys import stdin

def loading_list() -> list:
    string_list = []
    while True:
        string_element = stdin.readline().rstrip()
        if not string_element or string_element == '0':
            return string_list
        else:
            string_list.append(string_element)

number_list = loading_list()

def palindrome_checker(check_number:str) -> str:
    digits = len(check_number)
    for i in range(digits // 2):
        if check_number[i] != check_number[-i-1]:
            return "no"
    return "yes"

for i in number_list:
    print(palindrome_checker(i))