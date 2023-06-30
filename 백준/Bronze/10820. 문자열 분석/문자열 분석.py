# 10820 문자열 분석

while True:
    try:
        test = input()
        small, large, number, space = 0, 0, 0, 0
        for i in test:
            if ord("a") <= ord(i) <= ord("z"):
                small += 1
            elif ord("A") <= ord(i) <= ord("Z"):
                large += 1
            elif ord("0") <= ord(i) <= ord("9"):
                number += 1
            elif ord(i) == ord(" "):
                space += 1
        print(small, large, number, space)
    except:
        break