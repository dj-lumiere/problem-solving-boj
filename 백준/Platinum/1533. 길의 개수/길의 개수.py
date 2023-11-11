# 1533 길의 개수
from sys import stdin
from itertools import product


class Matrix:
    def __init__(self, matrix_values: list[list[int]]):
        self.val: list[list[int]] = matrix_values
        self.x_size: int = len(self.val[0])
        self.y_size: int = len(self.val)

    @staticmethod
    def identity(n: int) -> "Matrix":
        return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])

    @staticmethod
    def zero(n: int) -> "Matrix":
        return Matrix([[0 for _ in range(n)] for _ in range(n)])

    def __add__(self, other: "Matrix") -> "Matrix":
        if not (self.x_size == other.x_size and self.y_size == other.y_size):
            raise ValueError("You should have two identically sized matrix.")

        result = [[0 for _ in range(self.x_size)] for _ in range(self.y_size)]

        for i, j in product(range(self.x_size), range(self.y_size)):
            result[j][i] = self.val[j][i] + other.val[j][i]

        return Matrix(result)

    def __sub__(self, other: "Matrix") -> "Matrix":
        if not (self.x_size == other.x_size and self.y_size == other.y_size):
            raise ValueError("You should have two identically sized matrix.")

        result = [[0 for _ in range(self.x_size)] for _ in range(self.y_size)]

        for i, j in product(range(self.x_size), range(self.y_size)):
            result[j][i] = self.val[j][i] - other.val[j][i]

        return Matrix(result)

    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.x_size != other.y_size:
            raise ValueError(
                "The number of columns in the first matrix must equal the number of rows in the second matrix."
            )

        # Initialize the resulting matrix with zeros
        result = [[0 for _ in range(other.x_size)] for _ in range(self.y_size)]

        # Calculate matrix multiplication
        for i, j in product(range(self.y_size), range(other.x_size)):
            for k in range(self.x_size):
                result[i][j] += self.val[i][k] * other.val[k][j]

        return Matrix(result)

    def __iadd__(self, other: "Matrix") -> "Matrix":
        return self + other

    def __isub__(self, other: "Matrix") -> "Matrix":
        return self - other

    def __imul__(self, other: "Matrix") -> "Matrix":
        return self * other

    def mulmod(self, other: "Matrix", mod: int) -> "Matrix":
        if self.x_size != other.y_size:
            raise ValueError(
                "The number of columns in the first matrix must equal the number of rows in the second matrix."
            )

        # Initialize the resulting matrix with zeros
        result = [[0 for _ in range(other.x_size)] for _ in range(self.y_size)]

        # Calculate matrix multiplication
        for i, j in product(range(self.y_size), range(other.x_size)):
            for k in range(self.x_size):
                result[i][j] += self.val[i][k] * other.val[k][j]
            result[i][j] %= mod

        return Matrix(result)

    def __mulmod__(self, other: "Matrix", mod: int) -> "Matrix":
        if self.x_size != other.y_size:
            raise ValueError(
                "The number of columns in the first matrix must equal the number of rows in the second matrix."
            )

        # Initialize the resulting matrix with zeros
        result = [[0 for _ in range(other.x_size)] for _ in range(self.y_size)]

        # Calculate matrix multiplication
        for i, j in product(range(self.y_size), range(other.x_size)):
            result[i][j] = (
                sum(self.val[i][k] * other.val[k][j] for k in range(self.x_size)) % mod
            )

        return Matrix(result)

    # This is just for representation when you print the matrix
    def __str__(self) -> str:
        return "\n".join([" ".join(map(str, row)) for row in self.val])

    def matrix_square(self) -> "Matrix":
        if self.x_size != self.y_size:
            raise ValueError("Power of matrix is defined in square matrix.")
        return self * self

    def __exp__(self, index: int):
        if self.x_size != self.y_size:
            raise ValueError("Power of matrix is defined in square matrix.")
        result = Matrix.identity(self.x_size)
        while index:
            if index & 1:
                result *= self
            self *= self
            index >>= 1
        return result

    def pow(self, index: int, mod: int):
        if self.x_size != self.y_size:
            raise ValueError("Power of matrix is defined in square matrix.")
        result = Matrix.identity(self.x_size)
        while index:
            if index & 1:
                result = self.mulmod(result, mod)
            self = self.mulmod(self, mod)
            index >>= 1
        return result

    def __getitem__(self, index):
        return self.val[index]

    def __setitem__(self, index, value):
        self.val[index] = value


def input():
    return stdin.readline().strip()


N, S, E, T = map(int, input().split(" "))
matrix = Matrix([[0 for _ in range(5 * N)] for _ in range(5 * N)])
for i in range(N):
    for j in range(4):
        matrix[5 * i + j + 1][5 * i + j] += 1
path = [list(map(int, list(input()))) for _ in range(N)]
for i in range(N):
    for j in range(N):
        time = path[i][j]
        if time == 0:
            continue
        matrix[5 * i][5 * j + time - 1] += 1
matrix = matrix.pow(T, 1_000_003)
print(matrix[5 * S - 5][5 * E - 5])