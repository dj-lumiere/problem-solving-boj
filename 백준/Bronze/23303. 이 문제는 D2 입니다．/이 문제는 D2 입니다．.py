# 23303 이 문제는 D2 입니다.

question_string = list(input())
d2_checker = 0
for (i, j) in enumerate(question_string):
    if d2_checker == 0 and (j == "d" or j == "D"):
        d2_checker = 1
    elif d2_checker == 1 and j == "2":
        d2_checker = 2
        break
    elif d2_checker == 1 and not (j == "d" or j == "D") and j != "2":
        d2_checker = 0
print("D2" if d2_checker == 2 else "unrated")