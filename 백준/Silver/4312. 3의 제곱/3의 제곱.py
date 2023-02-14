import math
from sys import stdin

def n_ary_change(N: int, b: int):
    if N == 0:
        print("{ }")
    else:
        set_list = []
        for i in range(int(math.log(N, b))+1):
            mod:int = (N // (b**i))%b
            if mod:
                set_list.append(str(3**i))
        print("{",", ".join(set_list),"}")

def loading_list() -> list:
    string_list = []
    while True:
        string_element = stdin.readline().rstrip()
        if not string_element or string_element=='0':
            return string_list
        else:
            string_list.append(int(string_element))

for i in loading_list():
    n_ary_change(i-1,2)