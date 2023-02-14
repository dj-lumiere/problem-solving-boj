import sys

N = int(sys.stdin.readline().rstrip())

string_list = []
while True:
    try:
        string_element = sys.stdin.readline().rstrip()
        if string_element == "":
            raise EOFError
        else:
            string_list.append(int(string_element))
    except EOFError:
        break

def sol(N : int, unsorted_list : list[int]):
    unsorted_list.sort()
    for i in range(N):
        print(f"{unsorted_list[i]}")


sol(N, string_list)
