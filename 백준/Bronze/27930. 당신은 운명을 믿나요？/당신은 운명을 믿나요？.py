# A번 - 당신은 운명을 믿나요?

korea_finder: int = 0
yonsei_finder: int = 0
two_x_plus_1 = lambda x: (x << 1) + 1
jeomgwae = input()
pass_univ = ""
for i in jeomgwae:
    if i == "K" and korea_finder == 0:
        korea_finder = two_x_plus_1(korea_finder)
    elif i == "Y" and yonsei_finder == 0:
        yonsei_finder = two_x_plus_1(yonsei_finder)
    elif i == "O" and korea_finder == 1:
        korea_finder = two_x_plus_1(korea_finder)
    elif i == "O" and yonsei_finder == 1:
        yonsei_finder = two_x_plus_1(yonsei_finder)
    elif i == "R" and korea_finder == 3:
        korea_finder = two_x_plus_1(korea_finder)
    elif i == "N" and yonsei_finder == 3:
        yonsei_finder = two_x_plus_1(yonsei_finder)
    elif i == "S" and yonsei_finder == 7:
        yonsei_finder = two_x_plus_1(yonsei_finder)
    elif i == "E" and korea_finder == 7:
        korea_finder = two_x_plus_1(korea_finder)
    elif i == "E" and yonsei_finder == 15:
        yonsei_finder = two_x_plus_1(yonsei_finder)
    elif i == "A" and korea_finder == 15:
        pass_univ = "KOREA"
        break
    elif i == "I" and yonsei_finder == 31:
        pass_univ = "YONSEI"
        break
print(pass_univ)