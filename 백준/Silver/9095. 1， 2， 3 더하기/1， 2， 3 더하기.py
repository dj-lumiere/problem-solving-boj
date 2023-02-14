input_case = int(input())

def loading_list(item_count: int) -> list:
    string_list = []
    i = item_count
    while i:
        string_element = int(input())
        string_list.append(string_element)
        i -= 1
    return string_list

def sol(_N_ : int) -> int:
    if _N_ < 0:
        return 0
    elif _N_ == 1 or _N_ == 0:
        return 1
    else:
        return sol(_N_ - 1) + sol(_N_ - 2) + sol(_N_ - 3)

for i in loading_list(input_case):
    print(sol(int(i)))