N = int(input())

def negabinary_change(N: int):
    negabinary_list:list[str] = []
    if N == 0:
        negabinary_list = ["0"]
    else:
        while N:
            if N % -2:
                negabinary_list.append("1")
                N = (N-1) // -2
            else:
                negabinary_list.append("0")
                N = N // -2
    print("".join(negabinary_list[::-1]))

negabinary_change(N)