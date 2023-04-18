# 27299 헌내기 현철

# 10**7으로 A**(B**C)를 나눈 나머지
# m**k=m**(k+10**7) (mod 10**7) 이용

T = int(input())
for _ in range(T):
    value_list = input().split(" ")
    A = int(value_list[0])
    B = int(value_list[1])
    i = int(value_list[2])
    C = int(value_list[3][-7:])
    if C<=7 and B<=7:
        C_mod = C % (10**7)
        B_power_mod = pow(B, C_mod, 10**7)
    else:
        C_mod = C % (10**7) + 10**7
        B_power_mod = pow(B, C_mod, 10**7) + 10**7
    answer = pow(A, B_power_mod, 10**7)
    answer_formatted = f"{answer:0>7}"[::-1]
    print(answer_formatted[i])
