from sys import setrecursionlimit
setrecursionlimit(10**5)
N = int(input())

square_dict = {i**2: 1 for i in range(int(N**0.5), 0, -1)}
square_list = [i**2 for i in range(1, int(N**0.5) + 1)]


def minimum_squares_count(N):
    if N in square_dict:
        return square_dict[N]
    else:
        square_dict[N] = 1 + min(
            [
                square_dict[N - i]
                if N - i in square_dict
                else minimum_squares_count(N - i)
                for i in square_list[int(N**0.5 / 4) : int(N**0.5)]
            ]
        )
        return square_dict[N]


print(minimum_squares_count(N))