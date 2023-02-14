from sys import stdin, stdout

x, y = list(map(int, input().split(" ")))

def loading_dict_n(n: int) -> list:
    string_dict = dict()
    while n:
        n -= 1
        string_element = stdin.readline().rstrip()
        string_element1, string_element2 = list(map(str, string_element.split(" ")))
        string_dict[string_element1] = string_element2
    return string_dict

def loading_list_n(n: int) -> list:
    string_list = []
    while n:
        n -= 1
        string_element = stdin.readline().rstrip()
        string_list.append(string_element)
    return string_list

password_list = loading_dict_n(x)
password_find = loading_list_n(y)

def password_finder(id_pw_dict:dict, site_to_find: list) -> None:
    for i in site_to_find:
        if i in id_pw_dict:
            stdout.writelines(f"{id_pw_dict[i]}\n")

password_finder(password_list, password_find)
