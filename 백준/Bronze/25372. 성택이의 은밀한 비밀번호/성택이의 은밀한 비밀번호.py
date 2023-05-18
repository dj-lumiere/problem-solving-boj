# 25372 성택이의 은밀한 비밀번호
test_case_count = int(input())
for _ in range(test_case_count):
    test_string = input()
    if 6 <= len(test_string) <= 9:
        print("yes")
    else:
        print("no")