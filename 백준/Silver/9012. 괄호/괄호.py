def RightBracket():
    string = input()
    string = str(string)
    result_value = 0
    for i in range(len(string)):
        if string[i] == "(":
            result_value = result_value + 1
        elif string[i] == ")":
            result_value = result_value - 1
        if result_value < 0 :
            break
    if not result_value:
        print("YES")
    else:
        print("NO")

T = int(input())
for i in range(T):
    RightBracket()