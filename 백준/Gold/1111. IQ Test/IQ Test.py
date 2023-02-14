# 1111 IQ Test

N = int(input())
num_list = list(map(int, input().split(" ")))

def iq_test(N: int, num_list: list[int]):
    if N == 1:
        return "A"
    elif N == 2:
        if num_list[1] == num_list[0]:
            return num_list[0]
        else:
            # a*x(0)+b=x(1)
            # 베주의 방정식에 의해 해가 무한히 존재함이 보장된다.(gcd(x(0),1)=1)
            return "A"
    else:
        matrix_a = [[num_list[0],1],[num_list[1],1]]
        matrix_y = [num_list[1],num_list[2]]
        det = matrix_a[0][0]*matrix_a[1][1]-matrix_a[1][0]*matrix_a[0][1]
        matrix_a_inv = [[1,-1],[-1*num_list[1],num_list[0]]]
        a, b = [sum(matrix_a_inv[j][i]*matrix_y[i] for i in range(2)) for j in range(2)]
        if not det:
            if num_list[0] == num_list[1] and num_list[1] != num_list[2]:
                return "B"
            else:
                for i in range(3, N):
                    if num_list[i-1] != num_list[i]:
                        return "B"
                return num_list[N-1]
        if a % det or b % det:
            return "B"
        else:
            a, b = a//det, b//det
            for i in range(3, N):
                if num_list[i-1]*a+b != num_list[i]:
                    return "B"
            return num_list[N-1]*a+b

print(iq_test(N, num_list))
