matrix_size, index = list(map(int, input().split(" ")))
def sol(matrix_size:int, index:int):
    matrix = []
    for i in range(matrix_size):
        matrix_row = list(map(int, input().split(" ")))
        matrix.append(matrix_row)
    binary_index = [index//(2**i)%2 for i in range(37)]
    final_matrix = [[1 if i == j else 0 for i in range(matrix_size) ] for j in range(matrix_size)]
    def matrix_multiply(matrix_size:int, matrix1:list[list[int]], matrix2:list[list[int]]) -> list[list[int]]:
        new_matrix = [[0 for i in range(matrix_size)] for i in range(matrix_size)]
        for i in range(matrix_size):
            for j in range(matrix_size):
                new_matrix_element = 0
                for k in range(matrix_size):
                    new_matrix_element += matrix1[i][k]*matrix2[k][j]
                new_matrix[i][j] = new_matrix_element % 1000
        return new_matrix
    def matrix_square(matrix_size:int, matrix:list[list[int]]) -> list[list[int]]:
        return matrix_multiply(matrix_size, matrix, matrix)
    matrix_powered_dict = dict()
    matrix_powered_dict[0] = matrix
    for i in range(36):
        matrix_powered_dict[i+1] = matrix_square(matrix_size, matrix_powered_dict[i])
    for i, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply(matrix_size, final_matrix, matrix_powered_dict[i])
    return final_matrix

result = sol(matrix_size,index)
for i in result:
    print(" ".join(map(str, i)))