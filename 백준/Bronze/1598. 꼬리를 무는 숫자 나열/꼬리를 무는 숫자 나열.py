# 1598 꼬리를 무는 숫자 나열

A, B = map(int, input().split(" "))
A -= 1
B -= 1
A_row, A_col = divmod(A, 4)
B_row, B_col = divmod(B, 4)
print(abs(A_row - B_row) + abs(A_col - B_col))