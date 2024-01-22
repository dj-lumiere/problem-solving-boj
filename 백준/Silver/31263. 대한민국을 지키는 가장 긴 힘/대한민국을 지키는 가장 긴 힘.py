# A번 - 대한민국을 지키는 가장 긴 힘
INF = 10**18


def answer(string):
    cutting = [string[:1], string[:2], string[:3]]
    if not any(cutting):
        return 0
    possible_cutting = []
    possible_cutting_index = []
    for i, cut in enumerate(cutting):
        if cut[0] == "0":
            continue
        if not 1 <= int(cut) <= 641:
            continue
        possible_cutting.append(int(cut))
        possible_cutting_index.append(i + 1)
    if not possible_cutting:
        return INF
    return min(1 + answer(string[i:]) for i in possible_cutting_index)


_ = int(input())
string = input()
print(answer(string))