string_list = []
while True:
    try:
        string_element = input()
        if string_element == "":
            raise EOFError
        else:
            string_list.append(int(string_element))
    except EOFError:
        break

def sol(N : int, unsorted_list : list[int]):
    sort_memory = 0
    for i in range(N):
        for j in range(N-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                sort_memory = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = sort_memory
    for i in range(N):
        print(f"{unsorted_list[i]}")


sol(string_list[0], string_list[1:])