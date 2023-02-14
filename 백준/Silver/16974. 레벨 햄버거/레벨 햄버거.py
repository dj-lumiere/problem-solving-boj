def layer_count(N: int) -> int:
    if N == 0:
        return 1
    else:
        memo = 1
        for i in range(N):
            memo = 2 * memo + 3
        return memo

def patty_count(N: int) -> int:
    if N == 0:
        return 1
    else:
        memo = 1
        for i in range(N):
            memo = 2 * memo + 1
        return memo


def eaten_patty_count(N: int, eaten_layer_count: int) -> int:
    if eaten_layer_count == 0:
        return 0
    elif N == 0 and eaten_layer_count == 1:
        return 1
    elif N != 0 and eaten_layer_count == 1:
        return 0
    else:
        if eaten_layer_count == layer_count(N-1) + 2:
            return patty_count(N-1) + 1
        elif eaten_layer_count == layer_count(N):
            return patty_count(N)
        elif eaten_layer_count < layer_count(N-1) + 2:
            return eaten_patty_count(N-1, eaten_layer_count-1)
        else:
            return patty_count(N-1) + 1 + eaten_patty_count(N-1, eaten_layer_count - layer_count(N-1) - 2)
        
N, M = list(map(int, input().split(" ")))
print(eaten_patty_count(N, M))