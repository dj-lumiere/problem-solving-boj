# 1914 하노이 탑


def hanoi(n, source, auxiliary, destination):
    if n == 1:
        moves.append((source, destination))
        return
    hanoi(n - 1, source, destination, auxiliary)
    moves.append((source, destination))
    hanoi(n - 1, auxiliary, source, destination)


N = int(input())
K = 2**N - 1
moves = []
print(K)
if N <= 20:
    hanoi(N, 1, 2, 3)
    for move in moves:
        print(*move)