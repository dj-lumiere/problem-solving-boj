import sys

string_dict_N = dict()
string_list_M = []
string_element = ""
N = 0
M = 0

for i in range(1):
    string_element = sys.stdin.readline().rstrip("\n")
    N, M = list(map(int, string_element.split(" ")))

for i in range(N):
    string_element = sys.stdin.readline().rstrip()
    string_dict_N[string_element] = i

for i in range(M):
    string_element = sys.stdin.readline().rstrip()
    string_list_M.append(string_element)

def sol(_never_heard_ : dict[str], _never_seen_ : list[str]):
    count = 0
    never_heard_seen = []
    for i in _never_seen_:
        if i in _never_heard_:
            count += 1
            never_heard_seen.append(i)
    never_heard_seen.sort()
    print(count)
    for i in never_heard_seen:
        sys.stdout.writelines(f"{i}\n")

sol(string_dict_N, string_list_M)