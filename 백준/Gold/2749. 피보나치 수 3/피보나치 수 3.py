index = int(input())
def sol(index:int) -> list[list[int]]:
    # 피보나치 수열 => [[1,1],[1,0]]**n=[[F(n+1),F(n)],[F(n),F(n-1)]]
    matrix = [[1,1],[1,0]]
    binary_index = [index//(2**i)%2 for i in range(64)]
    # 2*2 단위 행렬 세팅
    final_matrix = [[1 if i == j else 0 for i in range(2)] for j in range(2)]
    # 2*2 행렬 곱셈 정의
    def matrix_multiply(matrix1:list[list[int]], matrix2:list[list[int]]) -> list[list[int]]:
        new_matrix = [[0 for i in range(2)] for i in range(2)]
        for i in range(2):
            for j in range(2):
                new_matrix_element = 0
                for k in range(2):
                    new_matrix_element += matrix1[i][k]*matrix2[k][j]
                new_matrix[i][j] = new_matrix_element % 1000000
        return new_matrix
    # 2*2 행렬 제곱 정의
    def matrix_square(matrix:list[list[int]]) -> list[list[int]]:
        return matrix_multiply(matrix, matrix)
    # A**(2**n)에 대한 행렬을 세팅해두기
    matrix_powered_dict = dict()
    matrix_powered_dict[0] = matrix
    for i in range(64):
        matrix_powered_dict[i+1] = matrix_square(matrix_powered_dict[i])
    # binary_index의 원소 중 1인 것들만 곱하기
    for i, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[i])
    return final_matrix

result = sol(index-1)[0][0]
print(result)