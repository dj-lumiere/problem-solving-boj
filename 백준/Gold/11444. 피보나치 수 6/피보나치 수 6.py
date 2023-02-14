index = int(input())
def sol(index:int):
    matrix = [[1,1],[1,0]]
    binary_index = [index//(2**i)%2 for i in range(64)]
    final_matrix = [[1 if i == j else 0 for i in range(2)] for j in range(2)]
    def matrix_multiply(matrix1:list[list[int]], matrix2:list[list[int]]) -> list[list[int]]:
        new_matrix = [[0 for i in range(2)] for i in range(2)]
        for i in range(2):
            for j in range(2):
                new_matrix_element = 0
                for k in range(2):
                    new_matrix_element += matrix1[i][k]*matrix2[k][j]
                new_matrix[i][j] = new_matrix_element % 1000000007
        return new_matrix
    def matrix_square(matrix:list[list[int]]) -> list[list[int]]:
        return matrix_multiply(matrix, matrix)
    matrix_powered_dict = dict()
    matrix_powered_dict[0] = matrix
    for i in range(64):
        matrix_powered_dict[i+1] = matrix_square(matrix_powered_dict[i])
    for i, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[i])
    return final_matrix

result = sol(index-1)[0][0]
print(result)