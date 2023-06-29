# 11719 그대로 출력하기 2

string_lines = []
while True:
    try:
        string_sub = input()
        string_lines.append(string_sub)
    except:
        break
print(*string_lines, sep="\n")